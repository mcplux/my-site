from django.contrib import admin
from .models import Home, About

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('name', 'occupation')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)
