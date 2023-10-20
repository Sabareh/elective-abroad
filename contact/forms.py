from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone', 'institution', 'program', 'how_did_you_hear', 'inquiry', 'passport', 'cv', 'transcript']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['passport'].label = 'Passport Upload'
        self.fields['cv'].label = 'CV Upload'
        self.fields['transcript'].label = 'Transcript Upload'
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['institution'].widget.attrs.update({'class': 'form-control'})
        self.fields['program'].widget.attrs.update({'class': 'form-control'})
        self.fields['how_did_you_hear'].widget.attrs.update({'class': 'form-control'})
        self.fields['inquiry'].widget.attrs.update({'class': 'form-control'})
        self.fields['passport'].widget.attrs.update({'class': 'form-control'})
        self.fields['cv'].widget.attrs.update({'class': 'form-control'})
        self.fields['transcript'].widget.attrs.update({'class': 'form-control'})


