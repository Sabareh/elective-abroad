from django.urls import path
from . import views

app_name = 'contact'  # Optional: You can set a namespace for the app

urlpatterns = [
    # Define your URL patterns here
    path('', views.contact, name='contact_form'),
    path('success/', views.form_success, name='contact_success'), 
]



