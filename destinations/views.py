from django.shortcuts import render

# Create your views here.
# destinations/views.py
from django.shortcuts import render
from .models import Destination

def destination_list(request):
    destinations = Destination.objects.all()
    return render(request, 'destinations/destination_list.html', {'destinations': destinations})

def destination_detail(request, pk):
    destination = Destination.objects.get(pk=pk)
    return render(request, 'destinations/destination_detail.html', {'destination': destination})

def program_detail(request, pk):
    program = ProgramDetails.objects.get(pk=pk)
    return render(request, 'destinations/program_detail.html', {'program': program})

def program_dates(request, pk):
    program = ProgramDetails.objects.get(pk=pk)
    return render(request, 'destinations/program_dates.html', {'program': program})

def program_fees(request, pk):
    program = ProgramDetails.objects.get(pk=pk)
    return render(request, 'destinations/program_fees.html', {'program': program})

def program_apply(request, pk):
    program = ProgramDetails.objects.get(pk=pk)
    return render(request, 'destinations/program_apply.html', {'program': program})

def program_apply_success(request, pk):
    program = ProgramDetails.objects.get(pk=pk)
    return render(request, 'destinations/program_apply_success.html', {'program': program})

def program_apply_fail(request, pk):
    program = ProgramDetails.objects.get(pk=pk)
    return render(request, 'destinations/program_apply_fail.html', {'program': program})

def program_apply_pending(request, pk):
    program = ProgramDetails.objects.get(pk=pk)
    return render(request, 'destinations/program_apply_pending.html', {'program': program})

def program_apply_complete(request, pk):
    program = ProgramDetails.objects.get(pk=pk)
    return render(request, 'destinations/program_apply_complete.html', {'program': program})