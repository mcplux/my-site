from django.db import models
from apps.common.models import SocialLink
from apps.projects.models import Project

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

class Portfolio(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    projects = models.ManyToManyField(Project)

    class Meta:
        verbose_name_plural = 'Portfolio'

class Contact(models.Model):
    title = models.CharField(max_length=30)
    
    class Meta:
        verbose_name_plural = 'Contact'
