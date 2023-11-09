from .models import CommentBook
from django.forms import ModelForm, EmailInput, Textarea

class CommentBookForm(ModelForm):
    class Meta:
        model = CommentBook
        fields = ['email', 'text']

        widgets = {
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Comment'
            })
        }