from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.basic, name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout,name='logout'),
    path('add/',views.add,name='add'),
    path('spsignup/',views.spsignup,name='spsignup'),
    path('splogin/',views.splogin,name='splogin'),
    path('spadditem/',views.spadditem,name="spadditem"),
    path('adding/',views.adding,name='adding'),
    path('servicereq/',views.servicereq,name='servicereq'),
    path('geolocation/',views.geolocation,name='geolocation')




]
