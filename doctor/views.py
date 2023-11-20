from django.shortcuts import render, redirect
from django.urls import reverse

# from django.shortcuts import reverse
from django.views.generic import (CreateView, ListView, UpdateView, DeleteView)
from . models import Services



class ServicesCreateView(CreateView):
    model = Services
    fields = ['name', 'description']
    # the template that will render the data/form.
    template_name = 'hospital/services_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_title'] = 'Add A New Service'
        print(context)
        return context
    def get_success_url(self) -> str:
        return reverse('services-list')
    
class ServicesListView(ListView):
    model = Services
    template_name = 'hospital/services_list.html'
    context_object_name = 'services'
    ordering = ['-pk']
    paginate_by = 10

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context
    
class ServicesDeleteView(DeleteView):
    model = Services
    success_url = '/'
    template_name = 'users/confirm_delete.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Service'
        service_name = Services.objects.get(pk=self.kwargs.get('pk')).name
        context['message'] = f'Are you sure you want to delete "{service_name}" ?'
        context['cancel_url'] = 'services-list'
        print(context)
        return context