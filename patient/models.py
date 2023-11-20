'''from django.db import models

from doctor.models import Doctor

class Patient(models.Model):
    gender_choices = (
                ('woman', "woman"),('men', "men"))
    
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    phone = models.CharField(max_length=12,default="",unique=True)
    gender = models.CharField(choices=gender_choices, max_length=30)
    
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name='appointments')
    
    
    def __str__(self):
        return f"{self.name}-{self.doctor.name}"
	'''