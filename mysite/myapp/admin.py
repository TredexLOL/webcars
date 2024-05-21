from django.contrib import admin
from .models import Car
class CarAdmin(admin.ModelAdmin):
    list_display = ('mark', 'model', 'year', 'transmission', 'mileage','fuel', 'price', 'date_posted')
    list_filter = ('mark', 'transmission', 'year')
    search_fields = ('mark', 'model')

admin.site.register(Car, CarAdmin)

