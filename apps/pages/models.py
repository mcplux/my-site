from django.db import models

class Home(models.Model):
    name = models.CharField(max_length=30)
    occupation = models.CharField(max_length=30)
    image = models.ImageField(upload_to='home/')

    class Meta:
        verbose_name_plural = 'Home'

class About(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    class Meta:
        verbose_name_plural = 'About'
