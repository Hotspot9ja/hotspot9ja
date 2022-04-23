from django.urls import path
from api.views import HomeAPIView


app_name = 'api'

urlpatterns = [
    path('', HomeAPIView.as_view(), name='home'),
]
