from django.shortcuts import render
from .models import *

from django.db.models import Max

# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    return render(request,'register.html')
def sangeethhos(request):
    return render(request,'sangeethhos.html')
def about(request):
    return render(request,'about.html')
def password(request):
    return render(request,'password.html')
def contactus(request):
    return render(request,'contactus.html')
def payment(request):
    return render(request,'payment.html')



def home(request):
    hos=Hospital.objects.all()
    d=Doctor.objects.all()
    context={'hos': hos,'d': d}
    return render(request,'home.html',context)
def doctorsprofile(request):
    id=request.GET.get('id')
    doc=Doctor.objects.filter(id=int(id))
    context={'doc':doc}
    return render(request,'doctorsprofile.html',context)
def bookslot(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        date=request.POST['date']
        time=request.POST['time']
        doctor=request.POST['doctor']
        gender=request.POST['gender']
        new_slot=appointment(name=name,email=email,phone=phone,date=date,time=time,doctor=doctor,gender=gender)
        new_slot.save()

    doc=Doctor.objects.all()
    context={'doc':doc}
    
    return render(request,'bookslot.html',context)













#............................................................................................................


def ret_details(request):
    text=Text.objects.all()
    d={'text':text}
    return render(request, 'index.html',d)
def ret_img(request):
    image=Hospital.objects.all()  
    e={'homepic':image}
    return render(request, 'index.html',e)
#..............................................................................


def login2(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pwd = request.POST.get('pwd')
        #print(un,pwd)
        #query to select a record based on a condition
        ul = login.objects.filter(username=un, password=pwd)
        

        if len(ul) == 1:
            request.session['user_name'] = ul[0].username
            request.session['userid'] = ul[0].id
            context2 = {'uname': request.session['user_name']}
            return render(request,'.home.html',context2)
        else:
            msg = '<h1> Invalid UserName or Password !!!</h1>'
            context ={ 'msg1':msg }
            return render(request, 'index.html',context)
    else:
        msg = ''
        context ={ 'msg1':msg }
        return render(request,'login.html')
    
#...........................................................

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
    
def view_hospital(request,pk):
    hosp=Hospital.objects.get(id=pk)
    doctors=Doctor.objects.filter(hospital=hosp)
    d=Doctor.objects.all()
    hos=Hospital.objects.all()
    context={ 'hosp':hosp,'doctors':doctors,'d':d,'hos':hos}
    return render(request,'hospital.html',context)

    