from django.contrib import admin
from .models import Home, About, Portfolio, Contact

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('name', 'occupation')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('title',)
