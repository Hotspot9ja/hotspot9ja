from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Contact, Profile, Producer, Artist, Commedian, Dj
# Sign Up Form
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2', 
            ]
        
# Profile Form
class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [
            'profile_image',
            'about',
            'company',
            'job',
            'country',
            'address',
            'phone',
            'twitter_url',
            'facebook_url',
            'instagram_url',
            'linkedin_url'
        ]

class UserEditForm(forms.ModelForm):
    
    class Meta:
        model = User
        verbose_name = 'User edit profile'
        verbose_name_plural = 'User edit profile'
        fields = [
            'first_name', 
            'last_name', 
            'email',
        ]
        
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        verbose_name = 'edit profile'
        verbose_name_plural = 'edit profile'
        fields = [
            'profile_image',
            'about',
            'company',
            'job',
            'country',
            'phone',
            'twitter_url',
            'facebook_url',
            'instagram_url',
            'linkedin_url'
        ]
class Producer(forms.ModelForm):
    class Meta:
        model = Producer
        fields = [
            'first_name',
            'last_name',
            'email',
            'location'
        ]
        
class Artist(forms.ModelForm):
    class Meta:
        model = Artist
        fields = [
            'first_name',
            'last_name',
            'email',
            'location'
        ]
        
class Commedian(forms.ModelForm):
    class Meta:
        model = Commedian
        fields = [
            'first_name',
            'last_name',
            'email',
            'location'
        ]
    
class Dj(forms.ModelForm):
    class Meta:
        model = Dj
        fields = [
            'first_name',
            'last_name',
            'email',
            'location'
        ]
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'subject',
            'message'
        ]
        
    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass