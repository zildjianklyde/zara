from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView  # Import the views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # Home page
    path('about/', AboutPageView.as_view(), name='about'),  # About page
    path('contact/', ContactPageView.as_view(), name='contact'),  #

]