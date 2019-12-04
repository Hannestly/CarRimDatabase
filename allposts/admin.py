from django.contrib import admin
from .models import Listing,Car,Rim,Manufacturer
# Register your models here.

admin.site.register(Listing)
admin.site.register(Car)
admin.site.register(Rim)
admin.site.register(Manufacturer)