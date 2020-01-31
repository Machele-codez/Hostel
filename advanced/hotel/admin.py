from django.contrib import admin
from hotel import models
# Register your models here.
admin.site.register(models.Tenant)
admin.site.register(models.Room)