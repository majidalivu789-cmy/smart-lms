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


class StudentReview(models.Model):
    student_name = models.CharField(max_length=100)
    student_role = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)
    profile_image = models.ImageField(upload_to='testimonial/', blank=True, null=True)
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['display_order', '-created_at']

    def __str__(self):
        return f"{self.student_name} ({self.rating}/5)"


