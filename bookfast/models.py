from django.db import models

# Create your models here.
class login(models.Model):
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.user_name
    
class registartion(models.Model):
    user_id=models.IntegerField(null=True)
    gender=models.CharField(max_length=20,null=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=100)
    date_of_birth=models.CharField(max_length=8)

    def __str__(self):
        return self.name

class Hospital(models.Model):
    hospital_name = models.CharField(max_length=255)
    hospital_address = models.CharField(max_length=100)
    hospital_no = models.CharField(max_length=10,null=True)
    hospital_dec = models.CharField(max_length=255)
    hospital_img=models.ImageField(upload_to='uploads/hospital/')

    def __str__(self):
        return self.hospital_name
    
class Doctor(models.Model):
    doctor_name = models.CharField(max_length=255)
    doctor_speciality = models.CharField(max_length=255)
    doctor_no = models.CharField(max_length=10,null=True)
    doctor_img=models.ImageField(upload_to='uploads/doctor/')
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    doctor_email = models.CharField(max_length=255)
    doctor_present = models.CharField(max_length=255)
    doctor_previous = models.CharField(max_length=255)

    def __str__(self):
        return self.doctor_name


class appointment(models.Model):
    appo_date=models.CharField(max_length=10)
    appo_time=models.CharField(max_length=10,null=True)
    patient_name=models.CharField(max_length=200)
    doc_name=models.CharField(max_length=200)
    patient_gen=models.CharField(max_length=50,null=True)
    patient_email=models.CharField(max_length=50,null=True)
    patient_no=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.appo_date
    
class contact(models.Model):
    con_name=models.CharField(max_length=100,null=True)
    con_email=models.CharField(max_length=50,null=True)
    cont_mess=models.CharField(max_length=255,null=True)
    cont_sub=models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.con_name

class Text(models.Model):
    dis_text=models.CharField(max_length=300)

class rating(models.Model):
    hos = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    user = models.ForeignKey(registartion, on_delete=models.CASCADE)
    review =models.CharField(max_length=50,null=True)

    

