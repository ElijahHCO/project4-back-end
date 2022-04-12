from django.contrib import admin

# Register your models here.
from .models import Location
from .models import Equipment
admin.site.register(Location)
admin.site.register(Equipment)