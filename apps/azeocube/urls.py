from django.urls import path
from . import views

app_name = 'azeocube'

urlpatterns = [
    path('verify-azeoid/', views.verify_azeoid, name='verify_azeoid'),
    path('register-team/', views.register_team, name='register_team'),
]
