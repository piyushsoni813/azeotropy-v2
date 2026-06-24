from django.urls import path
from . import views  # Import views

urlpatterns = [
    path('', views.home, name='home'),
]
