from django.db import models
from apps.common.models import SocialLink
from apps.projects.models import Project


class BasePage(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    class Meta:
        abstract = True


class Home(models.Model):
    name = models.CharField(max_length=30)
    occupation = models.CharField(max_length=30)
    image = models.ImageField(upload_to="home/")
    social_links = models.ManyToManyField(SocialLink)

    class Meta:
        verbose_name_plural = "Home"


class About(BasePage):
    class Meta:
        verbose_name_plural = "About"


class Portfolio(BasePage):
    projects = models.ManyToManyField(Project, blank=True)

    class Meta:
        verbose_name_plural = "Portfolio"


class Contact(BasePage):
    content = None

    class Meta:
        verbose_name_plural = "Contact"
