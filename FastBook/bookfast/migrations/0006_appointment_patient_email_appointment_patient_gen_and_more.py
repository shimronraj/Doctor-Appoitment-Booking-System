# Generated by Django 4.1.7 on 2023-04-04 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookfast', '0005_doctor_remove_hospital_doctor_delete_doctors_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='patient_email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient_gen',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient_no',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
