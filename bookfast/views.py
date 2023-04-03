from django.shortcuts import render
from .models import *

from django.db.models import Max

# Create your views here.
def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html')
def register(request):
    return render(request,'register.html')
def sangeethhos(request):
    return render(request,'sangeethhos.html')
def medicalhos(request):
    return render(request,'medicalhos.html')
def cityhos(request):
    return render(request,'cityhos.html')
def hari(request):
    return render(request,'hari.html')
def deepak(request):
    return render(request,'deepak.html')
def arun(request):
    return render(request,'arun.html')
def bookslot(request):
    return render(request,'bookslot.html')
def prakash(request):
    return render(request,'prakash.html')
def aravind(request):
    return render(request,'aravind.html')
def vishnu(request):
    return render(request,'vishnu.html')
def arya(request):
    return render(request,'arya.html')
def jickson(request):
    return render(request,'jickson.html')
def akhil(request):
    return render(request,'akhil.html')
def about(request):
    return render(request,'about.html')
#............................................................................................................

def contactus(request):
    return render(request,'contactus.html')
def ret_details(request):
    text=Text.objects.all()
    d={'text':text}
    return render(request, 'index.html',d)
def ret_img(request):
    image=hospital.objects.all()  
    e={'homepic':image}
    return render(request, 'index.html',e)
#..............................................................................


def login2(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pwd = request.POST.get('pwd')
        #print(un,pwd)
        #query to select a record based on a condition
        ul = userlogin.objects.filter(username=un, password=pwd, user_type='user')
        ub = userlogin.objects.filter(username=un, password=pwd, user_type='admin')

        if len(ul) == 1:
            request.session['user_name'] = ul[0].username
            request.session['user_id'] = ul[0].id
            context2 = {'uname': request.session['user_name']}
            return render(request,'./lmsapp/studlogin.html',context2)
        elif len(ub) == 1:
            request.session['user_name'] = ub[0].username
            request.session['user_id'] = ub[0].id
            context1={'uname': request.session['user_name']}
            return render(request,'./lmsapp/adminfirst.html',context1)
        else:
            msg = '<h1> Invalid UserName or Password !!!</h1>'
            context ={ 'msg1':msg }
            return render(request, './lmsapp/login.html',context)
    else:
        msg = ''
        context ={ 'msg1':msg }
        return render(request,'login.html')

def register_client(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        date = request.POST.get("date")
        gender=request.POST.get('gender')
        username = email
        #status = "new"
        if login.objects.filter(user_name=email):
            msg = {'msg1': 'username already exist.....'}
            return render(request,'/register.html',msg)
        else:

            ul = login(user_name=email, password=password)
            ul.save()
            user_id = login.objects.all().aggregate(Max('id'))['id__max']

            ud = registartion(user_id=user_id,name=name, date_of_birth=date, gender=gender,address=address, phone_no=phone, email=email,password=password)
            ud.save()

            print(user_id)
            context = {'msg': 'User Registered'}
            return render(request, 'register.html',context)

    else:
        return render(request, 'register.html')
    