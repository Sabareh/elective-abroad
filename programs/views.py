from django.shortcuts import render, get_object_or_404
from .models import Program, Country, City, Facility

def explore_programs(request):
    # Fetch all active programs
    programs = Program.objects.filter(is_active=True)
    return render(request, 'programs/explore_programs.html', {'programs': programs})

def explore_programs_by_country(request, country_code):
    # Fetch programs by country
    country = get_object_or_404(Country, code=country_code)
    programs = Program.objects.filter(category__is_active=True, category__country=country)
    return render(request, 'explore_programs_by_country.html', {'country': country, 'programs': programs})

def explore_programs_by_city(request, city_id):
    # Fetch programs by city
    city = get_object_or_404(City, id=city_id)
    programs = Program.objects.filter(category__is_active=True, category__city=city)
    return render(request, 'explore_programs_by_city.html', {'city': city, 'programs': programs})

def elective_facilities(request):
    # Fetch all elective facilities
    facilities = ElectiveFacility.objects.filter(is_active=True)
    return render(request, 'elective_facilities.html', {'facilities': facilities})

def program_detail(request, program_id):
    # Fetch program details
    program = get_object_or_404(Program, id=program_id)
    return render(request, 'program_detail.html', {'program': program})
