from django.contrib import admin

from .models import File, Test, Patient

admin.site.register(File)
admin.site.register(Test)
admin.site.register(Patient)