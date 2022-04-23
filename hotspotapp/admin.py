from django.contrib import admin
from .models import Producer, Artist, Commedian, Dj

# Register your models here.
@admin.register(Producer, Artist, Commedian, Dj)
class ProducerAdmin(admin.ModelAdmin):
    pass

class ArtistAdmin(admin.ModelAdmin):
    pass


class CommedianAdmin(admin.ModelAdmin):
    pass

class DjAdmin(admin.ModelAdmin):
    pass
    