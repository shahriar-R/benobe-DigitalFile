from django.db import models
from django.contrib.auth import get_user_model
import datetime



User = get_user_model()

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
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    

    def __str__(self):
        return self.name
    

'''
class Receptionist(models.Model):
	name = models.CharField(max_length=40)
	phone = models.CharField(max_length=12,default="",unique=True)
	doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
	username = models.OneToOneField(User,on_delete = models.CASCADE)
     
    '''
class Services(models.Model):
    name = models.CharField(max_length=100)
    # Column holds a brief description of the service
    description =models.TextField(max_length=500, help_text="Provide a description of the Service")

    #Method returns a string representation of the name of the service being provided by the hospital
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Services"

class Secretary(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE,related_name= "secretery") #user foreign key
    doctor = models.ForeignKey(Doctor, on_delete= models.SET_NULL,null=True ,related_name='doctor')
    username = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=11)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
