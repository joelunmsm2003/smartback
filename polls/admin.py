from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import *




@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    
