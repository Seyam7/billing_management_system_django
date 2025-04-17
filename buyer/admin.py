from django.contrib import admin

# Register your models here.
from .models import BuyerTable,Report

admin.site.register(BuyerTable)
admin.site.register(Report)
