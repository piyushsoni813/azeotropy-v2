from django.contrib import admin
from .models import User_Chem_e_cross
from import_export.admin import ImportExportModelAdmin
# Register your models here.
 
@admin.register(User_Chem_e_cross)
class userdetails(ImportExportModelAdmin):
    pass