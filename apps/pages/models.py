from django.db import models
from apps.common.models import SocialLink

class Home(models.Model):
    name = models.CharField(max_length=30)
    occupation = models.CharField(max_length=30)
    image = models.ImageField(upload_to='home/')
    social_links = models.ManyToManyField(SocialLink)

    class Meta:
        verbose_name_plural = 'Home'

class About(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    class Meta:
        verbose_name_plural = 'About'
