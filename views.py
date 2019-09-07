from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.conf import settings

from django.contrib.auth.decorators import login_required

from django.contrib import auth
from .models import memory
from .models import extenduser
from .models import serviceprovider
from .models import Experties
from math import ceil
from .models import Orders


# Create your views here.
#show diry
@login_required(login_url='/signup/login')
def basic(request):
    #log_user = request.user
    #memories = memory.objects.filter(user=log_user)
    experties = Experties.objects.all()
    print(experties)
    n = len(experties)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'expert':experties}
    return render(request,'signup/basic.html',params)#,{'m':memories}

#register function
def register(request):
    #to create a user
    if request.method == 'POST':
        if request.POST['password'] == request.POST['passwordagain']:
            #both the password are matched
            #now check if a previous user exist
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'signup/index.html', {'error':"User name alredy has taken"})

            except User.DoesNotExist:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['password'])
                names=request.POST['name']
                emails=request.POST['email']
                mobiles=request.POST['mobileno']
                citys=request.POST['city']
                states=request.POST['state']
                countrys=request.POST['country']
                pins=request.POST['pin']
                locations=request.POST['location']

                newextenduser=extenduser(name=names, email=emails, mobileno=mobiles, city=citys, state=states,
                                        country=countrys, pin=pins, location=locations, user=user)
                newextenduser.save()

                auth.login(request,user)
                return redirect(login)

        else:
            return render(request,'signup/index.html',{'error':"password do not match" })
    else:
     return render(request,'signup/index.html')

#login function
def login(request):
    if request.method == 'POST':
        #check if a user is exists
        #with the username and password

        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect(basic)
        else:
            return render(request,'signup/login.html',{'error':'invalid login credential'})


    return render(request,'signup/login.html')


#logout Function

def logout(request):
    return redirect(login)



#add try for diry data
@login_required(login_url='/signup/login/')
def add(request):
    if request.method=='POST':
        data=request.POST['data']
        new=memory(content=data,user=request.user)
        new.save()
        return render(request,'signup/basic.html')


    else:
     return render(request,'signup/mydiry.html')


#function for service provider
def spsignup(request):
    #to create a user
    if request.method == 'POST':
        if request.POST['password'] == request.POST['passwordagain']:
            #both the password are matched
            #now check if a previous user exist
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'signup/spsignup.html', {'error':"User name alredy has taken"})

            except User.DoesNotExist:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['password'])
                names=request.POST['name']
                emails=request.POST['email']
                mobiles=request.POST['mobileno']
                citys=request.POST['city']
                states=request.POST['state']
                countrys=request.POST['country']
                pins=request.POST['pin']
                locations=request.POST['location']
                experties = request.POST['experties']

                newserviceprovider=serviceprovider(name=names, email=emails, mobileno=mobiles, city=citys, state=states,
                                        country=countrys, pin=pins, location=locations, user=user, experties_id = int(experties))
                newserviceprovider.save()

                auth.login(request,user)
                return redirect(splogin)

        else:
            context_data = {
                'experties': Experties.objects.all(),
                'error':"Password do not match",
            }
            return render(request,'signup/spsignup.html', context_data)
    else:
        context_data = {
            'experties': Experties.objects.all(),
        }
        return render(request,'signup/spsignup.html', context_data)



#service provider login function
def splogin(request):
     if request.method == 'POST':
            #check if a user is exists
            #with the username and password

            user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
            if user is not None:
                auth.login(request,user)
                return redirect(spadditem)
            else:
                return render(request,'signup/splogin.html',{'error':'invalid login credential'})


     return render(request,'signup/splogin.html')



#add item service provider
def spadditem(request):
    return render(request,'signup/spadditem.html')



    #service provider add experties
def adding(request):
    names=request.POST['name']
    ctg = request.POST['category']
    sbctg=request.POST['subcategory']
    desc=request.POST['description']
    prices=request.POST['price']
    img=request.POST['myfile']
    experties=Experties(ename=names,ecategory=ctg,esubcategory=sbctg,edescription=desc,eprice=prices,eimage=img)
    experties.save()
    return redirect('home')

def servicereq(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        mobileno=request.POST.get('mobileno')
        zipcode=request.POST.get('zipcode')

        order=Orders(name=name,email=email,address=address,state=state,mobileno=mobileno,zipcode=zipcode)
        print('Hello')
        emails = EmailMessage("Request is raised", 'body goes here',settings.EMAIL_HOST_USER , [email])
        emails.send()
        print('BYe')
        order.save()



    return render(request,'signup/servicereq.html')


#get current location user by geolocation
def geolocation(request):
    return render(request,'signup/geolocation.html')
