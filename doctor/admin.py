from django.contrib import admin

from .models import Doctor, Services

admin.site.register(Doctor)
admin.site.register(Services)