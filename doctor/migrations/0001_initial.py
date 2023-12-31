# Generated by Django 3.2 on 2023-12-04 08:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('image', models.ImageField(default='default.png', upload_to='profile_pics')),
                ('department', models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('Dermatologist', 'Dermatologist'), ('Emergency Medicine Specialist', 'Emergency Medicine Specialist'), ('Allergist/Immunologist', 'Allergist/Immunologist'), ('Anesthesiologist', 'Anesthesiologist'), ('Colon and Rectal Surgeon', 'Colon and Rectal Surgeon')], default='Cardiologist', max_length=50)),
                ('speciality', models.CharField(max_length=120)),
                ('dob', models.DateField(default=datetime.date.today)),
                ('picture', models.ImageField(upload_to='doctors/')),
                ('address', models.CharField(default='address', max_length=300)),
                ('details', models.TextField()),
                ('experience', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Doctor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(help_text='Provide a description of the Service', max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Secretary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=11)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctor', to='doctor.doctor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secretery', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
