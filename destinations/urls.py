# destinations/urls.py
from django.urls import path
from . import views

app_name = 'destinations'

urlpatterns = [
    path('', views.destination_list, name='destination_list'),
    path('<int:pk>/', views.destination_detail, name='destination_detail'),
    path('program/<int:pk>/', views.program_detail, name='program_detail'),
    path('program/<int:pk>/dates/', views.program_dates, name='program_dates'),
    path('program/<int:pk>/fees/', views.program_fees, name='program_fees'),
    path('program/<int:pk>/apply/', views.program_apply, name='program_apply'),
    path('program/<int:pk>/apply/success/', views.program_apply_success, name='program_apply_success'),
    path('program/<int:pk>/apply/fail/', views.program_apply_fail, name='program_apply_fail'),
    path('program/<int:pk>/apply/pending/', views.program_apply_pending, name='program_apply_pending'),
    path('program/<int:pk>/apply/complete/', views.program_apply_complete, name='program_apply_complete'),
    
]
