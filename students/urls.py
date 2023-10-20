# students/urls.py
from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('profile/<int:student_id>/', views.student_profile, name='student_profile'),
    # Define more URL patterns as needed

]
