from django import forms
from .models import FAQ

class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = [
            'question',
            'answer',
        ]
        labels = {
            'question': 'Question',
            'answer': 'Answer',
        }
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control'}),
            'answer': forms.Textarea(attrs={'class': 'form-control'}),
        }
    
    def clean_question(self):
        question = self.cleaned_data.get('question')
        if len(question) < 5:
            raise forms.ValidationError("Question must be at least 5 characters long.")
        elif len(question) > 255:
            raise forms.ValidationError("Question must be less than 255 characters long.")
        else:
            return question
    