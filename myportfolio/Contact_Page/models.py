from django.db import models
from django.utils import timezone


# Create your models here.

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    reply = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    replied_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.name
    


from django.db import models
class MapSide(models.Model):
    Address = models.CharField(max_length=200)
    PhoneNumber = models.CharField(max_length=14)
    Email = models.CharField(max_length=200)
    MapLink = models.TextField()
    def __str__(self):
        return self.Address
    
