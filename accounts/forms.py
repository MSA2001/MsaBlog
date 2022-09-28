from django import forms
from django.contrib.auth import authenticate
from django.forms import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"input100"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"input100"}))
    
    def clean_password(self):
        user = authenticate( username=self.cleaned_data.get('username') , password=self.cleaned_data.get('password'))
        if user is not None:
            return self.cleaned_data.get('password')
        raise ValidationError("Invalid username/password",code='invalid_login')