from django.contrib import admin
from .models import Home, About, Portfolio, Contact


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ("name", "occupation", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
