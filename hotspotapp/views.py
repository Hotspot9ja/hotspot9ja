from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, FormView
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import ContactForm, SignUpForm, ProfileForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

# rest framework 
# from rest_framework import generics
from .models import Artist, Producer, Commedian, Dj, Profile
from api.serializers import ArtistSerializer

# Create your views here.
class HomePageView(TemplateView, FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = '/'
    
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)
    
class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
    
class ServicesPageView(TemplateView):
    template_name = 'pages/services.html'
    
class PortfolioPageView(TemplateView):
    template_name = 'pages/portfolio.html'
    
class PortfolioDetailView(TemplateView):
    template_name = 'pages/portfolio-details.html'
    
class TermPageView(TemplateView):
    template_name = 'pages/terms.html'
    
class PrivacyPolicyPageView(TemplateView):
    template_name = 'pages/privacy_policy.html'
    
class BlogPageView(TemplateView):
    template_name = 'pages/blog.html'
    


# Sign Up View
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('hotspotapp:profile')
    template_name = 'registration/signup.html'
    
# Edit Profile View
class ProfileView(LoginRequiredMixin, TemplateView):
    model = Profile
    template_name = 'registration/profile.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['profile'] = Profile.objects.all()
        return context
    
  

    
    
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'
    
class UserProfile(LoginRequiredMixin, FormView):
    template_name = 'dashboard/users-profile.html'
    form_class = ProfileForm
class EditProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = EditProfileForm
    template_name = ''
# class ArtistAPIView(generics.ListAPIView):
#     queryset = Artist.objects.all()
#     serializer_class = ArtistSerializer
    
