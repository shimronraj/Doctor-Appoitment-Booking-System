from django.db import models

# Create your models here.
class login(models.Model):
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    
class registartion(models.Model):
    user_id=models.IntegerField(null=True)
    gender=models.CharField(max_length=20,null=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=100)
    date_of_birth=models.CharField(max_length=8)
   
class doctors(models.Model):
    doctor_name = models.CharField(max_length=255)
    doctor_speciality = models.CharField(max_length=255)
    doctor_no = models.IntegerField()
    doctor_img=models.ImageField(upload_to='uploads/doctor/')

class hospital(models.Model):
    hospital_name = models.CharField(max_length=255)
    hospital_address = models.CharField(max_length=100)
    hospital_no = models.IntegerField()
    hospital_dec = models.CharField(max_length=255)
    doctor=models.ForeignKey(doctors,on_delete=models.CASCADE)
    hospital_img=models.ImageField(upload_to='uploads/hospital/')
class appointment(models.Model):
    appo_date=models.CharField(max_length=10)
    appo_time=models.IntegerField()
    patient_name=models.CharField(max_length=200)
    doc_name=models.CharField(max_length=200)
class Text(models.Model):
    dis_text=models.CharField(max_length=300)

