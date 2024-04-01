from  django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomerRegistration(UserCreationForm,):
    username=forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True','class':'forms-control'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'forms-control'}))
    password1=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'forms-control'}))
    password2=forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'forms-control'}))