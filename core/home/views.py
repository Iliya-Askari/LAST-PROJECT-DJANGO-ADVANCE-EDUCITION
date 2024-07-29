from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class IndexView(TemplateView):
    template_name = 'home/index.html'

class AboutView(TemplateView):
    template_name = 'home/about.html'
    
class ContactView(TemplateView):
    template_name = 'home/contact.html'
    
class TeamView(TemplateView):
    template_name = 'team/team.html'

class TeamDetailsView(TemplateView):
    template_name = 'team/team-details.html'