from tkinter import Widget
from django import forms 
from django.core.validators import ValidationError

from blog.models import Message

        
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude =('user','email')
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px;"
            }),
            "text": forms.Textarea(attrs={
                "class": "form-control",
            }),
            "email": forms.TextInput(attrs={
                "class": "form-control",
            }),
        }
   