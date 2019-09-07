from __future__ import unicode_literals
from django.db import models
import datetime
from django.contrib.auth.models import User

#Create your models here.
class memory(models.Model):
    content=models.TextField()
    date=models.DateField(("date"), default=datetime.date.today)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

class extenduser(models.Model):
    userid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email= models.EmailField(max_length=100)
    mobileno = models.IntegerField()
    city = models.CharField(max_length=50,)
    state = models.CharField(max_length=50,)
    country = models.CharField(max_length=50,)
    pin = models.IntegerField()
    location = models.CharField(max_length=50,)
    user=models.OneToOneField(User,on_delete=models.CASCADE,)

    def __str__(self):
        return self.name

class Experties(models.Model):
    #eid = models.AutoField(primary_key=True)
    ename=models.CharField(max_length=50)
    ecategory=models.CharField(max_length=50)
    esubcategory=models.CharField(max_length=50)
    edescription=models.CharField(max_length=100)
    eprice=models.IntegerField()
    eimage=models.ImageField(upload_to='signup/images')

    def __str__(self):
        return self.ename

#class for service ServiceProvider
class serviceprovider(models.Model):
    #userid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email= models.EmailField(max_length=100)
    mobileno = models.IntegerField()
    city = models.CharField(max_length=50,)
    state = models.CharField(max_length=50,)
    country = models.CharField(max_length=50,)
    pin = models.IntegerField()
    location = models.CharField(max_length=50,)

    experties = models.ForeignKey(Experties, on_delete=models.CASCADE, null=True, blank=True)


    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Orders(models.Model):
    #o_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    mobileno = models.IntegerField(default=0)
    email=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=100)
    #amount=models.IntegerField()

    def __str__(self):
        return self.name

#current location for Maps
class Venue(models.Model):

    name = models.CharField(max_length=255)

    latitude = models.DecimalField(
                max_digits=9, decimal_places=6, null=True, blank=True)

    longitude = models.DecimalField(
                max_digits=9, decimal_places=6, null=True, blank=True)



class Incidence(models.Model):
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Meta:
    verbose_name_plural="Incidence"
