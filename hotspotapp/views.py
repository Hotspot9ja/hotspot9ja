from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import SignUpForm, ProfileForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

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
class ProfileView(LoginRequiredMixin, CreateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('hotspotapp:dashboard')
    template_name = 'registration/profile.html'
    
    def form_valid(self, form):
        form.instance.user=self.request.user
        form.save()
        return super().form_valid(form)
    
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'
class EditProfileView(UpdateView):
    model = User
    form_class = EditProfileForm
    template_name = ''
class ArtistAPIView(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer