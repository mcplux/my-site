from django.db import models
from colorfield.fields import ColorField


class SocialLink(models.Model):
    name = models.CharField(max_length=30)
    url = models.URLField()
    order = models.PositiveIntegerField(default=0)
    icon = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("order",)


class Skill(models.Model):
    TYPE_CHOICES = (
        ("lang", "Language"),
        ("front", "Frontend"),
        ("back", "Backend"),
        ("db", "Database"),
    )
    name = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    order = models.PositiveBigIntegerField(default=0)
    bg_color = ColorField(
        default="#ffffff",
        blank=True,
        verbose_name="Background color",
    )
    text_color = ColorField(default="#000000", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("order",)
