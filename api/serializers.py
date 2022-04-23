from rest_framework import serializers
from hotspotapp.models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    model = Artist
    fields = [
        'first_name',
        'last_name',
        'email',
        'location'
    ]