from django import forms
from django.db import models
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Enter username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Enter password'}))
    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Enter name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Enter lastname'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Enter username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Enter E-Mail'}))
    height = forms.CharField(widget=forms.NumberInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Enter height (in centimeters)'}))
    weight = forms.CharField(widget=forms.NumberInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Enter weight (in kilograms)'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Confirm your password'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'height', 'weight', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'readonly': True}))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'readonly': True}))
    height = forms.FloatField(widget=forms.NumberInput(attrs={
        'class': 'form-control py-4'}), min_value=0)
    weight = forms.FloatField(widget=forms.NumberInput(attrs={
        'class': 'form-control py-4'}), min_value=0)
    bmi = forms.FloatField(widget=forms.NumberInput(attrs={
        'class': 'form-control py-4', 'readonly': True}))
    bmi_status = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'readonly': True}), required=False)
    bmi_history = forms.JSONField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'readonly': True}), required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email', 'height', 'weight', 'bmi', 'bmi_status', 'bmi_history')
