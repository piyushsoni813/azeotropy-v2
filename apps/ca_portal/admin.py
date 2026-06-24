from django.contrib import admin
from .models import Extendeduser
from .models import Azeo_id_user
from import_export.admin import ImportExportModelAdmin
# Register your models here.
 
@admin.register(Extendeduser)
class userdetails(ImportExportModelAdmin):
    pass

@admin.register(Azeo_id_user)
class userdetails(ImportExportModelAdmin):
    pass