# Generated by Django 4.1.7 on 2023-04-08 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookfast', '0008_alter_appointment_appo_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('con_name', models.CharField(max_length=100, null=True)),
                ('con_email', models.CharField(max_length=50, null=True)),
                ('cont_mess', models.CharField(max_length=255, null=True)),
                ('cont_sub', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
