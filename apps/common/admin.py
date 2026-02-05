from django.contrib import admin
from django.utils.html import format_html
from .models import SocialLink, Skill


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "url")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "type", "preview")
    readonly_fields = ("preview",)

    def preview(self, obj):
        return format_html(
            '<div id="color-preview" style="padding:10px;background:{};color:{};">Preview</div>',
            obj.bg_color,
            obj.text_color,
        )

    class Media:
        js = ("js/color-preview.js",)
