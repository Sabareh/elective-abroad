from django.shortcuts import render
from .models import StudentProfile

def home(request):
    # Your view logic here
    return render(request, 'home.html')

def about_us(request):
    # Your view logic here
    return render(request, 'about-us.html')
    
def cookie-policy(request):
    return render(request, 'cookie-policy.html')
    
def student_profile(request, student_id):
    student = StudentProfile.objects.get(pk=student_id)
    return render(request, 'students/student_profile.html', {'student': student})  

def student_list(request):
    students = StudentProfile.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_list_by_country(request, country):
    students = StudentProfile.objects.filter(country=country)
    return render(request, 'students/student_list.html', {'students': students})

def student_list_by_university(request, university):
    students = StudentProfile.objects.filter(university=university)
    return render(request, 'students/student_list.html', {'students': students})



