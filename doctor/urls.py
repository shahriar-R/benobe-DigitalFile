from django.urls import path

from . import views

urlpatterns = [
    # path('register_adm/',views.register_adm_view,name='register_adm.html'),
    # path('registr_doce/',views.register_doc_view,name='register_doc.html'),
    path('services', views.ServicesListView.as_view(), name='services-list'),
    path('services/new/', views.ServicesCreateView.as_view(), name='services-create'),
    path('services/<int:pk>/delete/', views.ServicesDeleteView.as_view(), name='services-delete'),
    
]

