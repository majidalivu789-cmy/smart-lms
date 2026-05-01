from django.db import models
from Home_Page.models import Instructor

class myCourses(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True, blank=True, related_name='public_course_details')
    course_title = models.CharField(max_length=50)
    course_des = models.TextField(blank=True, default='')
    course_level = models.CharField(max_length=55,default="level")
    course_duration = models.CharField(max_length=55,default="dur")
    course_image = models.FileField(upload_to='courses/',max_length=250,null=True, default=None)
    course_price = models.CharField(max_length=100, blank=True, default='Free')
    course_lessons = models.CharField(max_length=55, blank=True, default='')
    course_language = models.CharField(max_length=55, blank=True, default='English / Urdu')
    course_outline = models.TextField(blank=True, default='', help_text='Write each outline point on a new line.')
    course_requirements = models.TextField(blank=True, default='', help_text='Write each requirement on a new line.')
    course_projects = models.TextField(blank=True, default='', help_text='Write each project/practice item on a new line.')
    course_outcomes = models.TextField(blank=True, default='', help_text='Write each learning outcome on a new line.')
    course_certificate = models.CharField(max_length=150, blank=True, default='Certificate guidance')
    course_support = models.CharField(max_length=150, blank=True, default='Student support')
    course_enroll_note = models.TextField(blank=True, default='Enroll to continue with this course and begin learning with Smart Learn LMS.')
    
# Create your models here.
