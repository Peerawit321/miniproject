from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.Home, name='Home'),
    path('Lockopen/',views.Lockopen, name='Lockopen')
]