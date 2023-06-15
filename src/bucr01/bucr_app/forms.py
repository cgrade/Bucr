#!/usr/bin/ python3

from django import forms 
from django.forms import modelformset_factory
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Restaurant, Review, Reservation, UserProfile, Photo
from django.forms import ClearableFileInput



class RestaurantRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    name = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea)
    cuisine_type = forms.CharField(max_length=100)
    address = forms.CharField(max_length=255)   
    contact_number = forms.CharField(max_length=15)
    opening_hours = forms.CharField(max_length=100)
    image = forms.ImageField(required=False)

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            restaurant = Restaurant.objects.create(
                user=user,
                name=self.cleaned_data['name'],
                description=self.cleaned_data['description'],
                cuisine_type=self.cleaned_data['cuisine_type'],
                address=self.cleaned_data['address'],
                contact_number=self.cleaned_data['contact_number'],
                opening_hours=self.cleaned_data['opening_hours'],
                image=self.cleaned_data['image']
            )
        return user

class MultiFileInput(forms.ClearableFileInput):
    template_name = 'bucr_app/templates/multi-file-input.html'

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'address', 'contact_number',
        'description', 'image', 'opening_hours']
        widgets = {'photo_gallery': MultiFileInput()}






class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['restaurant', 'images']
        widgets = {
            'images': MultiFileInput(),
        }

PhotoFormSet = modelformset_factory(Photo, form=PhotoForm, extra=1)

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'time', 'num_guests', 'table']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}),
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter your password'}),
    )


# User Profile Form

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'phone_number', 'image']


# user Registration Form
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
