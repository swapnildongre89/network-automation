from django.contrib import admin
from .models import Routers, Switches, Firewalls, Loadbalancers
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Routers, Switches, Firewalls, Loadbalancers)
class Admin(ImportExportModelAdmin):
    pass
