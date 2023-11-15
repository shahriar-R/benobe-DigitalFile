from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.forms.widgets import SelectDateWidget

from . import models

'''dep=[('Cardiologist','Cardiologist'),
('Dermatologist','Dermatologist'),
('Emergency Medicine Specialist','Emergency Medicine Specialist'),
('Allergist/Immunologist','Allergist/Immunologist'),
('Anesthesiologist','Anesthesiologist'),
('Colon and Rectal Surgeon','Colon and Rectal Surgeon')
]'''


class DoctorRegisterForm(UserCreationForm):
    
    # dep = [('Cardiologist','Cardiologist')] 
    username = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'placeholder': 'USERNAME'}))
    username.widget.attrs.update({'class' : 'app-form-control'})
    
    
    firstname = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'FIRSTNAME'}))
    firstname.widget.attrs.update({'class' : 'app-form-control'})
    
    lastname = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'LASTNAME'}))
    lastname.widget.attrs.update({'class' : 'app-form-control'})
    
    dob = forms.DateField(label="",widget=SelectDateWidget(years=range(1960, 2021)))
    dob.widget.attrs.update({'class' : 'app-form-control-date'})
    
    address = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'ADDRESS'}))
    address.widget.attrs.update({'class' : 'app-form-control'})
    
    city = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'CITY'}))
    city.widget.attrs.update({'class' : 'app-form-control'})
    
    
    
    
    image = forms.ImageField(label="")
    image.widget.attrs.update({'class' : 'app-form-control'})
    
    # department = forms.CharField(label="",widget = forms.Select(choices=dep))
    # department.widget.attrs.update({'class' : 'app-form-control'})

    password1 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'PASSWORD'}))
    password1.widget.attrs.update({'class' : 'app-form-control'})
    
    password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'RE-CONFIRM'}))
    password2.widget.attrs.update({'class' : 'app-form-control'})

    class Meta:
        model = User
        fields = ['username', 'firstname', 'lastname','department', 'dob', 'address', 'city',  'postalcode', 'password1', 'password2','image']
        #fields = ['username', 'email', 'firstname', 'lastname', 'age', 'dob', 'address', 'city', 'country', 'postalcode', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
    
    def checkdate(self):    #form date of birth validator
        cleaned_data = self.cleaned_data
        db = cleaned_data.get('dob')
        if db < timezone.now().date():
            return True
        self.add_error('dob', 'Invalid date of birth.')
        return False
    


class ReceptionistRegisterForm(UserCreationForm):  #used to register an admin
    username = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'placeholder': 'USERNAME'}))
    username.widget.attrs.update({'class' : 'app-form-control'})
    
    firstname = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'FIRSTNAME'}))
    firstname.widget.attrs.update({'class' : 'app-form-control'})
    
    lastname = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'LASTNAME'}))
    lastname.widget.attrs.update({'class' : 'app-form-control'})
    
    
    
    
    password1 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'PASSWORD'}))
    password1.widget.attrs.update({'class' : 'app-form-control'})
    
    password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'RE-CONFIRM'}))
    password2.widget.attrs.update({'class' : 'app-form-control'})

    class Meta:
        model = User
        fields = ['username', 'firstname', 'lastname', 'password1', 'password2']
        #fields = ['username', 'email', 'firstname', 'lastname', 'age', 'dob', 'address', 'city', 'country', 'postalcode', 'password1', 'password2']
        help_texts = {k:"" for k in fields}