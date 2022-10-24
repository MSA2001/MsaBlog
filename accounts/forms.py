from django import forms
from django.contrib.auth import authenticate
from django.forms import ValidationError
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "input100", "placeholder": "username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "input100", "placeholder": "Password"}))
    
    def clean_password(self):
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if user is not None:
            return self.cleaned_data.get('password')
        raise ValidationError("Invalid username/password", code='invalid_login')
    
    
class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "input100", "placeholder": "Username"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"class": "input100", "placeholder": "Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "input100", "placeholder": "Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "input100", "placeholder": "Confirm Password"}))

    def clean_username(self):
        user = User.objects.filter(username=self.cleaned_data.get('username')).exists()
        if user:
            raise forms.ValidationError('This username is already exist')
        else:
            return self.cleaned_data.get('username')

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise ValidationError('passwords are not match', code='invpass')



class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

