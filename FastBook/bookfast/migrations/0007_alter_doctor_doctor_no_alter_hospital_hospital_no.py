# Generated by Django 4.1.7 on 2023-04-04 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookfast', '0006_appointment_patient_email_appointment_patient_gen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='doctor_no',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='hospital_no',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
