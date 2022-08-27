from django.contrib import admin
from cars.models import Car

# Register your models here.

class MyCarAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Time information', { 'fields': ['year']}),
        ('Car information', { 'fields': ['brand']})
    ]

admin.site.register(Car, MyCarAdmin)