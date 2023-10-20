# contact/views.py
from django.shortcuts import render, redirect
from django.shortcuts import render
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact_form.html', {'form': form})


def form_success(request):
    return render(request, 'contact/contact_form_success.html')

def submissions_list(request):
    submissions = ContactFormSubmission.objects.all()
    return render(request, 'contact/submissions_list.html', {'submissions': submissions})   

def submission_detail(request, pk)  :
    submission = ContactFormSubmission.objects.get(pk=pk)
    return render(request, 'contact/submission_detail.html', {'submission': submission})    

def submission_delete(request, pk):
    submission = ContactFormSubmission.objects.get(pk=pk)
    submission.delete()
    return redirect('contact:submissions_list')     

def submission_update(request, pk):
    submission = ContactFormSubmission.objects.get(pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=submission)
        if form.is_valid():
            form.save()
            return redirect('contact:submissions_list')
    else:
        form = ContactForm(instance=submission)
    return render(request, 'contact/contact_form.html', {'form': form})


