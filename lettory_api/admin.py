from django.contrib import admin
from . import models

admin.site.register(models.UserData)
admin.site.register(models.Tickets)
admin.site.register(models.TotalData)
