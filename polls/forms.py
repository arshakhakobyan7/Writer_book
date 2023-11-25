from .models import CommentBook
from django.forms import ModelForm, EmailInput, Textarea, TextInput
from django.contrib.auth.models import User

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

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name',  'username', 'email', 'password']

        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Firstname'
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Lastname'
            }),
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'password': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            })
        }