from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    demo = models.URLField()
    repo = models.URLField()

    def __str__(self):
        return self.title
