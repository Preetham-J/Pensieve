from django.contrib import admin

#Import models
from .models import Todo

#Register models
admin.site.register(Todo)
