from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.validators import RegexValidator, validate_email
from .models import Profile

User._meta.get_field('email')._unique = True  # to make the email field unique


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_regex = RegexValidator(regex=r'^01[1250][0-9]{7,8}$', message="Enter an Egyptian phone number!")
    phone = forms.CharField(validators=[phone_regex], max_length=11)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'phone', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField(disabled=True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['country', 'facebook_profile', 'birth_date', 'image']
