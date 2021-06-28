from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class Website(models.Model):
    nom = models.CharField(max_length=255)
    logo = models.FileField(upload_to="website_image")
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Website'
        verbose_name_plural = 'Websites'

    def __str__(self):
        return self.nom


class Newletter(models.Model):
    email = models.EmailField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Newletter'
        verbose_name_plural = 'Newletters'

    def __str__(self):
        return self.email


class Configuration(models.Model):
    description_newletter = HTMLField()
    copyrights = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Configuration'
        verbose_name_plural = 'Configurations'

    def __str__(self):
        return self.copyrights


class SocialIcon(models.Model):
    nom = models.CharField(max_length=255)
    icone = models.CharField(max_length=255)
    lien = models.URLField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'SocialIcon'
        verbose_name_plural = 'SocialIcons'

    def __str__(self):
        return self.nom