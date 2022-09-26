from django import forms 
from django.core.validators import ValidationError

from blog.models import Message

class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=20,label='write your name here')
    text = forms.CharField(max_length=500,label='write your text here')
    
    def clean(self):
        name = self.cleaned_data.get('name')
        text = self.cleaned_data.get('text')
        if name == text:
            raise ValidationError('name and text are same',code='name_&_text')
        
        
        
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('__all__')
   