from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class ServicesView(TemplateView):
    template_name = 'services/services.html'

class ServicesDetailsView(TemplateView):
    template_name = 'services/services-details.html'
    
