from django.urls import path

from . import views

app_name = "ca_portal"



urlpatterns = [
    path('', views.Registration, name='index'),
    path('register/', views.user_register, name="register"),
    path('azeo_id/',views.AZeo_id, name='azeo_id'),
    
]
