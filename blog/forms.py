# blog/forms.py
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author_name', 'comment_text']
        labels = {'author_name': 'Your name', 'comment_text': 'Your comment'}
        widgets = {'comment_text': forms.Textarea(attrs={'rows': 3})}

        
