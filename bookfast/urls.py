from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns=[

    path('',views.ret_details,name='index'),
    path('index',views.ret_img,name='index'),
    path('home',views.home,name='home'),
    path('register',views.register_client,name='register'),
    path('login',views.login2,name='login'),
    path('contactus',views.contactus,name='contactus'),
    path('sangeethhos',views.sangeethhos,name='sangeethhos'),
    path('medicalhos',views.medicalhos,name='medicalhos'),
    path('cityhos',views.cityhos,name='cityhos'),
    path('hari',views.hari,name='hari'),
    path('deepak',views.deepak,name='deepak'),
    path('arun',views.arun,name='arun'),
    path('bookslot',views.bookslot,name='bookslot'),
    path('vishnu',views.vishnu,name='vishnu'),
    path('aravind',views.aravind,name='aravind'),
    path('prakash',views.prakash,name='prakash'),
    path('arya',views.arya,name='arya'),
    path('akhil',views.akhil,name='akhil'),
    path('jickson',views.jickson,name='jickson'),
    path('about',views.about,name='about'),

]