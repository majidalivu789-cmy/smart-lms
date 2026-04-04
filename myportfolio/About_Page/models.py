from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class AboutSml(models.Model):
    about_title = models.CharField(max_length=200)
    about_des = HTMLField()
    def __str__(self):
        return self.about_title

class AboutFeature(models.Model):
    feature_icon = models.CharField(max_length=155)
    feature_user = models.CharField(max_length=55)
    feature_title = models.CharField(max_length=300)
    def __str__(self):
        return self.feature_title


