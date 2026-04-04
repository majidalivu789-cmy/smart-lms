from django.db import models

class myCourses(models.Model):
    course_title = models.CharField(max_length=50)
    course_des = models.CharField(max_length=55)
    course_level = models.CharField(max_length=55,default="level")
    course_duration = models.CharField(max_length=55,default="dur")
    course_image = models.FileField(upload_to='courses/',max_length=250,null=True, default=None)
    
# Create your models here.
