from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'app/home.html'  # Indented correctly

class AboutPageView(TemplateView):  # Renamed the second class
    template_name = 'app/about.html'  # Indented correctly

class ContactPageView(TemplateView):  # Renamed the second class
    template_name = 'app/contact.html'  # Indented correctly
