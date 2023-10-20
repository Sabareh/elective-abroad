# pricing/urls.py
from django.urls import path
from . import views

app_name = 'pricing'

urlpatterns = [
    path('', views.pricing_list, name='pricing_list'),
    path('<int:program_id>/', views.pricing_detail, name='pricing_detail'),

]
