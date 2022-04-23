from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import SignUpForm, ProfileForm
from django.contrib.auth.models import User

# rest framework 
from rest_framework import generics
from .models import Artist, Producer, Commedian, Dj
from api.serializers import ArtistSerializer

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

# Sign Up View
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('hotspotapp:profile')
    template_name = 'registration/signup.html'
    
# Edit Profile View
class ProfileView(CreateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('hotspotapp:dashboard')
    template_name = 'registration/profile.html'
    
class ArtistAPIView(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer