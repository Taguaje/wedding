from django.contrib import admin
from .models import Guest, Menu, Dishes, Alcohol

# Register your models here.
admin.site.register(Guest)
admin.site.register(Menu)
admin.site.register(Dishes)
admin.site.register(Alcohol)
