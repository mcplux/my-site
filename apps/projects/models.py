from django.db import models
from apps.common.models import Skill

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    demo = models.URLField()
    repo = models.URLField()
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.title
