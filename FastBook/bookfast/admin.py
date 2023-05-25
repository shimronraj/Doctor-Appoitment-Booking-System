from django.contrib import admin
from .models import *


class HospitalAdmin(admin.ModelAdmin):
    list_display = ('hospital_name','hospital_address','hospital_no','hospital_dec','hospital_img')
# Register your models here.
admin.site.register(login)
admin.site.register(registartion)
admin.site.register(Hospital,HospitalAdmin)
admin.site.register(Doctor)
admin.site.register(appointment)
admin.site.register(Text)
admin.site.register(contact)
admin.site.register(rating)
