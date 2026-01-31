from django.contrib import admin
from .models import SocialLink, Skill


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "url")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "type", "bg_color", "text_color")
