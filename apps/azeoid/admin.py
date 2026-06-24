from django.contrib import admin
from .models import Registration

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'year_of_study', 'azeoid')
    search_fields = ('name', 'email')

admin.site.register(Registration, RegistrationAdmin)
