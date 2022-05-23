from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms 
from .models import UserProfile

class UserForm(UserCreationForm):
    """This form uses the built-in UserCreationForm to handle user creation"""
    first_name = forms.CharField(max_length=30, required=True,
                    widget=forms.TextInput(attrs={
                        'placeholder': '*Your first name'
                    }))

    last_name = forms.CharField(max_length=30, required=True,
                    widget=forms.TextInput(attrs={
                        'placeholder': '*Your last name'
                    }))

    username = forms.EmailField(max_length=254, required=True,
                    widget=forms.TextInput(attrs={
                        'placeholder': '*Email...'
                    }))
    
    password1 = forms.CharField(
                    widget=forms.PasswordInput(attrs={
                        'placeholder': '*Password'
                    }))

    password2 = forms.CharField(
                    widget=forms.PasswordInput(attrs={
                        'placeholder': '*Confirm Password'
                    }))

    # reCAPTCHA tooken 
    token = forms.CharField(
                    widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                    'password1', 'password2')


class AuthForm(AuthenticationForm):
    '''Form that uses built-in Authentication to handle user auth'''

    username = forms.EmailField(max_length=254, required=True,
                        widget=forms.TextInput(attrs={
                            'placeholder': '*Email...'
                        }))
                
    password = forms.CharField(
                            widget=forms.PasswordInput(attrs={
                                'placeholder': '*Password...'
                            }))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserProfileForm(forms.ModelForm):
    '''Basic model form for user profile thata extends django user model'''

    address = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    town = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    county = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    postal_code = forms.CharField(max_length=8, required=True, widget=forms.HiddenInput())
    country = forms.CharField(max_length=40, required=True, widget=forms.HiddenInput())
    longitude = forms.CharField(max_length=50, required=True, widget=forms.HiddenInput())
    latitude = forms.CharField(max_length=50, required=True, widget=forms.HiddenInput())

    class Meta:
        model = UserProfile
        fields = ('address', 'town', 'county', 
                    'postal_code', 'country', 
                    'longitude', 'latitude')
