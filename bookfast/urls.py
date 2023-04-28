from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns=[

    path('',views.ret_details,name='index'),
    path('index',views.ret_img,name='index'),
    path('home',views.home,name='home'),
    path('register',views.register_client,name='register'),
    path('payment',views.payment,name='payment'),
    
    path('contactus',views.contactus,name='contactus'),
    path('sangeethhos',views.sangeethhos,name='sangeethhos'),
    path('doctorsprofile',views.doctorsprofile,name='doctorsprofile'),

    path('login',views.login2,name='login'),
    
    
    path('rating',views.rating,name='rating'),
    path('bookslot',views.bookslot,name='bookslot'),
    path('about',views.about,name='about'),
    path('password',views.password,name='password'),
    path('hospital_detail/<int:pk>',views.view_hospital,name="hospital_details")

]