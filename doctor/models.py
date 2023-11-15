from django.db import models
from django.contrib.auth.models import User
import datetime





class Doctor(models.Model):
    departments=[('Cardiologist','Cardiologist'),   
('Dermatologist','Dermatologist'),
('Emergency Medicine Specialist','Emergency Medicine Specialist'),
('Allergist/Immunologist','Allergist/Immunologist'),
('Anesthesiologist','Anesthesiologist'),
('Colon and Rectal Surgeon','Colon and Rectal Surgeon')
]
    user =  models.ForeignKey(User, on_delete=models.CASCADE,related_name="Doctor") #user foreign key
    name = models.CharField(max_length=120)
    image = models.ImageField(default="default.png",upload_to="profile_pics")   #profile picture
    department= models.CharField(max_length=50,choices=departments,default='Cardiologist')  #doctor department from choices given as list
    speciality = models.CharField(max_length=120)
    dob = models.DateField(default=datetime.date.today) #doctor date of birth
    picture = models.ImageField(upload_to="doctors/")
    address = models.CharField(max_length=300,default="address")
    details = models.TextField()
    experience = models.TextField()
    
    

    def __str__(self):
        return self.name
    

class Receptionist(models.Model):
	name = models.CharField(max_length=40)
	phone = models.CharField(max_length=12,default="",unique=True)
	doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
	username = models.OneToOneField(User,on_delete = models.CASCADE)