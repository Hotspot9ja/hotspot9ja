from django.urls import path
from django.contrib.auth import views
from .views import HomePageView, SignUpView, ProfileView, DashboardView

from django.conf import settings
from django.conf.urls.static import static


app_name = 'hotspotapp'


urlpatterns = [
    
    path('accounts/login/', views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout'),
    path('accounts/password_change/', views.PasswordChangeView.as_view(template_name='change-password.html'), name='password_change'),
    path('accounts/password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('accounts/password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    # Sign Up
    path('signup/', SignUpView.as_view(), name='signup'),
    # profile 
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
    path('profile/dashboard/', DashboardView.as_view(), name='dashboard'),

    path('', HomePageView.as_view(), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
