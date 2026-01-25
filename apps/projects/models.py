from django.db import models
from apps.common.models import Skill


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    demo = models.URLField()
    repo = models.URLField()
    skills = models.ManyToManyField(Skill)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("order",)
