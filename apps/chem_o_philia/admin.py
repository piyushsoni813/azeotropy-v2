# Register your models here.
from django.contrib import admin
from .models import COPuser
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(COPuser)
class userdetails(ImportExportModelAdmin):
    pass