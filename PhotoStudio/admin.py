from django.contrib import admin

# Register your models here.
from .models import Appointments, Queries
admin.site.register(Appointments)
admin.site.register(Queries)

admin.site.site_header = 'Uk Photography Admin'