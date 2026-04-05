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


class FooterSettings(models.Model):
    site_name = models.CharField(max_length=100, default='Smart LMS')
    about_text = models.TextField()
    newsletter_text = models.CharField(max_length=255, default='Subscribe to get update about new courses.')
    newsletter_placeholder = models.CharField(max_length=100, default='Enter your email')
    newsletter_button_text = models.CharField(max_length=30, default='Subscribe')
    copyright_text = models.CharField(max_length=255)
    project_note = models.TextField(blank=True)

    def __str__(self):
        return self.site_name


class FooterLink(models.Model):
    SECTION_CHOICES = (
        ('quick', 'Quick Links'),
        ('course', 'Courses'),
    )
    section = models.CharField(max_length=10, choices=SECTION_CHOICES)
    label = models.CharField(max_length=100)
    url = models.CharField(max_length=255, default='#')
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order', 'id']

    def __str__(self):
        return f"{self.get_section_display()} - {self.label}"


class FooterContact(models.Model):
    icon_class = models.CharField(max_length=80, default='fas fa-angle-right')
    value = models.CharField(max_length=255)
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order', 'id']

    def __str__(self):
        return self.value


class FooterSocialLink(models.Model):
    platform = models.CharField(max_length=40)
    icon_class = models.CharField(max_length=80)
    url = models.CharField(max_length=255, default='#')
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order', 'id']

    def __str__(self):
        return self.platform

