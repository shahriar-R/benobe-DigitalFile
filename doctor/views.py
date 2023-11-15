from django.shortcuts import render, redirect
from datetime import date,timedelta,time
from django.contrib.auth.models import User,Group
from django.utils import timezone

from .models import Doctor
from .forms import DoctorRegisterForm, ReceptionistRegisterForm


def register_doc_view(request):
    if request.method=="POST":
        form = DoctorRegisterForm(request.POST, request.FILES)
        if form.is_valid(): #if form is valid
            db = form.cleaned_data.get('dob')   #get date of birth from form
            if db < timezone.now().date():  #if date of birth is valid
                nu = User.objects.create_user(username=form.cleaned_data.get('username'),email=form.cleaned_data.get('email'),password=form.cleaned_data.get('password1'))  #create new user
                doc = Doctor(user=nu,firstname=form.cleaned_data.get('firstname'),
                        lastname=form.cleaned_data.get('lastname'),
                        department=form.cleaned_data.get('department'),
                        dob=form.cleaned_data.get('dob'),
                        address=form.cleaned_data.get('address'),
                        city=form.cleaned_data.get('city'),
                        country=form.cleaned_data.get('country'),
                        postalcode=form.cleaned_data.get('postalcode'),
                        image=request.FILES['image'])   #create new doctor
                doc.save()
                dp = DoctorProfessional(doctor=doc,appfees=200,admfees=2000)    #ccreate doctor professional model instance using default prices
                dp.save()
                mpg = Group.objects.get_or_create(name='DOCTOR')    #add user to doctor group
                mpg[0].user_set.add(nu)
                return redirect('login_doc.html')
            else:   #if date of birth is invalid
                form.add_error('dob', 'Invalid date of birth.')
                return render(request,'hospital/Doctor/register_doc.html',{'form': form})
        else:
            print(form.errors)
    else: 
        form = DoctorRegisterForm()
    
    return render(request,'hospital/Doctor/register_doc.html',{'form': form})




def register_adm_view(request):
    if request.method=="POST":
        form = ReceptionistRegisterForm(request.POST, request.FILES)
        if form.is_valid():     #get data from form (if it is valid)
            db = form.cleaned_data.get('dob')   #get date of birth from form
            today = date.today()
            ag =  today.year - db.year - ((today.month, today.day) < (db.month, db.day))    #calculate age from dob
            if db < timezone.now().date():  #check if date of birth is valid (happened the previous day or even back)
                nu = User.objects.create_user(username=form.cleaned_data.get('username'),email=form.cleaned_data.get('email'),password=form.cleaned_data.get('password1'))  #create user
                # adm = Admin(user=nu,firstname=form.cleaned_data.get('firstname'),
                #             lastname=form.cleaned_data.get('lastname'),
                #             age=ag,
                #             dob=form.cleaned_data.get('dob'),
                #             address=form.cleaned_data.get('address'),
                #             city=form.cleaned_data.get('city'),
                #             country=form.cleaned_data.get('country'),
                #             postalcode=form.cleaned_data.get('postalcode'),
                #             image=request.FILES['image']
                #             )   #create admin
                # adm.save()
                mpg = Group.objects.get_or_create(name='ADMIN') #add user to admin group
                mpg[0].user_set.add(nu)
                return redirect('login_adm.html')
            else:
                form.add_error('dob', 'Invalid date of birth.')
        else:
            print(form.errors)
            return render(request,'hospital/Admin/register_adm.html',{'form': form})
    else: 
        form = AdminRegisterForm()
    
    return render(request,'hospital/Admin/register_adm.html',{'form': form})