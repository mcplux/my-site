from django.db import models


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
    )
    name = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    order = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("order",)
