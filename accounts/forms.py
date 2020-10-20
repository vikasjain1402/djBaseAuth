
from django import forms
from django.forms import PasswordInput
class Loginform(forms.Form):
    username=forms.CharField(max_length=100,label='username')
    password=forms.CharField(max_length=20,label='password',widget=PasswordInput())

class Signupform(forms.Form):
    username=forms.CharField(max_length=100,label='username')
    password=forms.CharField(max_length=20,label='password',widget=PasswordInput())
    confirm_password = forms.CharField(max_length=20, label='confirm Password',widget=PasswordInput())
    email = forms.EmailField(max_length=100, label='email')
    firstname= forms.CharField(max_length=100, label='first name')
    lastname=forms.CharField(max_length=100,label='last name')




