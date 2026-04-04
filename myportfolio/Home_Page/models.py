from django.db import models

# Create your models here.
class Logo(models.Model):
    nav_logo =models.FileField(upload_to='background/',max_length=250,null=True, default=None)
    nav_title =models.CharField(max_length=200)
    def __str__(self):
        return self.nav_title

class FounderMessage(models.Model):
    visit_founder = models.CharField(max_length=200)
    message_title = models.CharField(max_length=300)
    founder_message = models.TextField()
    founder_name = models.CharField(max_length=200)
    def __str__(self):
        return self.message_title

class Feature(models.Model):
    feature_icon = models.CharField(max_length=300)
    feature_title = models.CharField(max_length=150)
    feature_des = models.TextField()
    def __str__(self):
        return self.feature_title
    
class Instructor(models.Model):
    instruct_img = models.FileField(upload_to='instructors/',max_length=250,null=True, default=None)
    instruct_name = models.CharField(max_length=55)
    instruct_skill = models.CharField(max_length=55)
    about_instruct = models.TextField()
    def __str__(self):
        return self.instruct_name

class Top_Courses(models.Model):
       course_image = models.FileField(upload_to='courses/',max_length=250,null=True, default=None)
       course_title = models.CharField(max_length=150)
       course_des =models.TextField()
       course_duration = models.CharField(max_length=55)
       course_price = models.CharField(max_length=100)
       def __str__(self):
              return self.course_title

