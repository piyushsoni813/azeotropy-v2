from django.urls import path

from . import views

app_name = "cop"

urlpatterns = [
    path('/',views.user_register, name = 'register'),
]