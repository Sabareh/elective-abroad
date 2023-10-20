from django.shortcuts import render
from .models import ProgramPricing

def pricing_list(request):
    pricing = ProgramPricing.objects.all()
    return render(request, 'pricing/pricing_list.html', {'pricing': pricing})

def pricing_detail(request, program_id):
    pricing = ProgramPricing.objects.get(id=program_id)
    return render(request, 'pricing/pricing_detail.html', {'pricing': pricing})



