
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # User management
    path('accounts/', include('django.contrib.auth.urls')),
    
    # local app 
    path('', include('hotspotapp.urls')),
     # api 
    path('api/', include('api.urls')),
]
