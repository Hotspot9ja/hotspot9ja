from django.contrib import admin
from .models import Contact, Producer, Artist, Commedian, Dj, Profile

# Register your models here.
@admin.register(Producer, Artist, Commedian, Dj, Profile, Contact)
class ProducerAdmin(admin.ModelAdmin):
    pass

class ArtistAdmin(admin.ModelAdmin):
    pass


class CommedianAdmin(admin.ModelAdmin):
    pass

class DjAdmin(admin.ModelAdmin):
    pass
    
class ProfileAdmin(admin.ModelAdmin):
    pass

class ContactAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'subject',
        'message'
    ]