from django.urls import path

from . import views

urlpatterns = [
    path('register_adm/',views.register_adm_view,name='register_adm.html'),
    path('register_doc/',views.register_doc_view,name='register_doc.html'),
]

