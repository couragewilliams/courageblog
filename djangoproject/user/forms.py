from cProfile import Profile
from dataclasses import field
import email
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
class UserUpadteForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
        
class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model=Profile
        fields=['bio','passport']