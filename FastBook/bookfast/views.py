from django.shortcuts import redirect, render
from .models import *
from io import BytesIO
from django.http import HttpResponse
from django.db.models import Max
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


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



def payment(request,id):
    if request.method == 'POST':
        id=request.POST["hospital_id"]
        r=f"http://127.0.0.1:8000/bookslot/{id}"
        return redirect(r)
    else:
        return render(request,'payment.html',{'hospital_id':id})


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
def bookslot(request,pk):
    hos=Hospital.objects.get(id=pk)
    doc=Doctor.objects.filter(hospital=hos)
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        date=request.POST['date']
        time=request.POST['time']
        doctor=request.POST['doctor']
        gender=request.POST['gender']
        if appointment.objects.filter(appo_time=time,doc_name=doctor,appo_date=date):
            msg="Slot Already Booked"
            context={'doc':doc,'msg':msg}
    
            return render(request,'bookslot.html',context)
        new_slot=appointment(patient_name=name,patient_email=email,patient_no=phone,appo_date=date,appo_time=time,doc_name=doctor,patient_gen=gender)
        new_slot.save()
        pdf_file = generate_pdf(new_slot)
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="receipt.pdf"'
        return response
    
    context={'doc':doc}
    
    return render(request,'bookslot.html',context)
def contactus(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['subject']
        new_contact=contact(con_name=name,con_email=email,cont_sub=subject,cont_mess=message)
        new_contact.save()
    return render(request,'contactus.html')

def search_doctors(request):
    search_query = request.GET.get('search_query')
    doctors = Doctor.objects.all()

    if search_query:
        doctors = doctors.filter(doctor_name__icontains=search_query)

    context = {
        'search_query': search_query,
        'doctors': doctors
    }
    return render(request, 'search_doctors.html', context)




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
        ul = login.objects.filter(user_name=un, password=pwd)
        

        if len(ul) == 1:
            request.session['user_name'] = ul[0].user_name
            request.session['userid'] = ul[0].id
            context2 = {'uname': request.session['user_name']}
            return redirect(home)
        else:
            msg = '<h1> Invalid UserName or Password !!!</h1>'
            context ={ 'msg1':msg }
            return render(request, 'login.html',context)
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
            return render(request,'register.html',msg)
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
    hos=Hospital.objects.filter(id=pk)
    hos2=Hospital.objects.get(id=pk)
    context={ 'hosp':hosp,'doctors':doctors,'d':d,'hos':hos,'k':hos2}
    return render(request,'hospital.html',context)


#.................................................................receipt
def generate_pdf(new_slot):
    # Create a file-like buffer to receive PDF data.
    buffer = BytesIO()

    # Create the PDF object, using the BytesIO object as its "file."
    p = canvas.Canvas(buffer, pagesize=letter)
    # Register the Arial font.
    pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))
    # Set the font style.
    p.setFont("Arial", 16)
    p.rect(20, 20, 550, 770)

    # Add a header.
    header_text = 'Book Fast'
    p.drawString(200, 750, header_text)
    p.drawString(210, 690, 'Booking Details')
    p.drawString(200, 450, 'Thank you!!!')
    p.drawString(472, 720, 'Ernakulam')
    \

    # Create bullet point list.
    bullet_list = []
    bullet_list.append('Name of the Patient:------------------------------ ' + new_slot.patient_name)
    bullet_list.append('Doctors Name:------------------------------------- ' + new_slot.doc_name)
    bullet_list.append('Issued Date:-------------------------------------- ' + new_slot.appo_date)
    bullet_list.append('Issued Time:-------------------------------------- ' + new_slot.appo_time)
    bullet_list.append('Phone Number:------------------------------------- ' + new_slot.patient_no)
    

    # Add bullet points.
    y = 600
    for bullet in bullet_list:
        p.drawString(130, y, bullet)
        y -= 20

    # Add a footer.
    footer_text = 'Page %s' % p.getPageNumber()
    p.drawString(450, 50, footer_text)

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return buffer

#................................................................rating

def rate(request):
    id= request.GET.get("id")
    r= Hospital.objects.get(id=int(id))
    u = request.session['user_name'] 
    user = registartion.objects.get(email=u)
    if request.method == "POST":
        name = request.POST.get('rate')
        rat=rating(review=name , user=user , hos=r)
        rat.save()
        # new_rating=rating(review=name, user=user, hos=r)
        # new_rating.save()
        return redirect('home')
    else:
        return render(request, 'rating.html')


