from django.shortcuts import render
from django.views.generic import ListView

from hotspotapp.models import Artist

# Create your views here.

class HomeAPIView(ListView):
    model = Artist
    template_name = 'artist_list.html'
