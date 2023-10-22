from django.shortcuts import render, get_object_or_404, redirect
from .models import FAQ
from .forms import FAQForm  # You can create a form for creating or updating FAQs

def faq_list(request):
    faqs = FAQ.objects.all()
    return render(request, 'faq/faq_list.html', {'faqs': faqs})

def faq_detail(request, faq_id):
    faq = get_object_or_404(FAQ, pk=faq_id)
    return render(request, 'faq/faq_detail.html', {'faq': faq})

def faq_create(request):
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            faq = form.save()
            return redirect('faq:faq_detail', faq_id=faq.pk)
    else:
        form = FAQForm()
    return render(request, 'faq/faq_form.html', {'form': form})

def faq_update(request, faq_id):
    faq = get_object_or_404(FAQ, pk=faq_id)
    if request.method == 'POST':
        form = FAQForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            return redirect('faq:faq_detail', faq_id=faq.pk)
    else:
        form = FAQForm(instance=faq)
    return render(request, 'faq/faq_form.html', {'form': form, 'faq': faq})

def faq_delete(request, faq_id):
    faq = get_object_or_404(FAQ, pk=faq_id)
    if request.method == 'POST':
        faq.delete()
        return redirect('faq:faq_list')
    return render(request, 'faq/faq_confirm_delete.html', {'faq': faq})
