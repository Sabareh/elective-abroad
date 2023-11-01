from django.urls import path
from . import views

app_name = 'programs'

urlpatterns = [
    path('', views.explore_programs, name='explore_programs'),
    path('explore_programs/<str:country_code>/', views.explore_programs_by_country, name='explore_programs_by_country'),
    path('explore-programs/cities/<int:city_id>/', views.explore_programs_by_city, name='explore_programs_by_city'),
    path('elective-facilities/', views.elective_facilities, name='elective_facilities'),
    path('program_detail/<int:program_id>/', views.program_detail, name='program_detail'),
]
