from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Dashboard Courses Data
class DashboardCourse(models.Model):
    course_icon = models.CharField(max_length=200)
    course_title = models.CharField(max_length=200)
    course_fees = models.CharField(max_length=55)
    def __str__(self):
        return self.course_title
    
# Change Profile Image of the Student
class ProfileImage(models.Model):
    photo = models.ImageField(upload_to='User_Profile',default="default/user.png", blank=True, null=True)

# ====================Student Form==============
class Student(models.Model):
    
    GENDER_CHOICE = [('Male','Male'),
                     ('Female','Female'),
                     ('Other','Other')]
    
    COUNTRY_CHOICE = [('Pakistan','Pakistan')]

    PROVINCE_CHOICE = [
        ('Punjab','Punjab'),
        ('Sindh','Sindh'),
        ('khyber_pakhtunkhwa','Khyber Pakhtunkhwa'),
        ('Balochistan','Balochistan'),
        ]
    PHONE_CODE =[
        ('+92','+92 (Pakistan)')
    ]

    EDUCATION_CHOICE = [
        ('Matric','Matric'),
        ('Inter','Intermediate'),
        ('Bs','Bachelor (BS)'),
        ('Master','Master (MS / MA / MSc)'),
        ('Mphill','MPhill'),
        ('phd','PhD'),
    ]

    name = models.CharField(max_length=55)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICE)
    date_of_birth = models.DateField()
    cnic = models.CharField(max_length=15)
    country = models.CharField(max_length=55,choices=COUNTRY_CHOICE,default='Pakistan')
    province = models.CharField(max_length=55,choices=PROVINCE_CHOICE)
    district = models.CharField(max_length=55)
    address = models.TextField()
    phone_code = models.CharField(max_length=55,choices=PHONE_CODE)
    phone = models.CharField(max_length=10)
    education = models.CharField(max_length=55,choices=EDUCATION_CHOICE)


def __init__(self, *args, **kwargs):
    super().__init__(self, *args, **kwargs)
    self.fields['province'].empty_label= 'Select Province'

# Week Model Course-Wise 
class CourseWeek(models.Model):
    course = models.ForeignKey(
        DashboardCourse,
        on_delete= models.CASCADE,
        related_name = "weeks"
    )
    week_number = models.PositiveBigIntegerField()

    def __str__(self):
        return f"{self.course.course_title} - Week {self.week_number}"
    
# Lecture Model Week Wise 
class CourseLecture(models.Model):
    week = models.ForeignKey(
        CourseWeek,
        on_delete = models.CASCADE,
        related_name = "lectures"
    )
    title = models.CharField(max_length=200)
    video_url = models.URLField()

    def __str__(self):
        return self.title
    
# ========= Fees Payment integration ====
class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    course = models.ForeignKey(DashboardCourse, on_delete = models.CASCADE)
    is_paid = models.BooleanField(default = False)
    enrolled_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        unique_together = ('user', 'course')
    
    def __str__(self):
        return f"{self.user.username} - {self.course.course_title}"
    
# ====== News and Events Page ======
class Updates(models.Model):
    # Rigt side Tags 
    TAG_CHOICE = (
        ('news', 'News'),
        ('event', 'Event'),
        ('announcement', 'Announcement'),
        ('course', 'Course'),

    )
    
    BUTTON_CHOICES = [
        ('read', 'Read More'),
        ('register', 'Register Now'),
        ('schedule', 'View Schedule'),
        ('course', 'Go to Course'),
    ]

    updation_date = models.DateField()
    updation_title = models.CharField(max_length = 255)
    updation_desc = models.TextField()
    updation_tag = models.CharField(max_length=55, choices = TAG_CHOICE)
    button_type = models.CharField(max_length=55, choices= BUTTON_CHOICES)
    button_link = models.CharField(max_length=255)

    def __str__(self):
        return self.updation_title

# ======== Important Links =======
class ImportantLinks(models.Model):

    ICON_CHOICES = [
            ('fa-solid fa-file-pdf', 'PDF'),
            ('fa-solid fa-file-word', 'Word'),
            ('fa-solid fa-video', 'Video'),
            ('fa-solid fa-link', 'Link'),
        ]
    link_title = models.CharField(max_length = 255)
    link_desc = models.TextField()
    link_icon = models.CharField(max_length=55, default='fa-solid fa-link', choices=ICON_CHOICES)
    important_link = models.URLField()
    is_new = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.link_title
    
# Dynamic Video Page
# ===== Video Progress Tracking =====
class VideoProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lecture = models.ForeignKey(CourseLecture, on_delete=models.CASCADE)
    watched = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'lecture')

    def __str__(self):
        return f"{self.user.username} - {self.lecture.title} - {self.watched}"

# ====== Dynamic Quiz Page ========

# Quiz Model
# Is model ko replace karein (models.py mein)
class Quiz(models.Model):
    # NEW FIELD: Ab har quiz ek specific course se link hoga
    course = models.ForeignKey(DashboardCourse, on_delete=models.CASCADE, related_name="quizzes", null=True, blank=True)
    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=100)  # fontawesome class
    total_questions = models.IntegerField()
    time = models.IntegerField()  # minutes
    start_date = models.DateTimeField(null=True, blank=True)
    expiry_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.course.course_title if self.course else 'No Course'})"


# Question Model
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.TextField()

    def __str__(self):
        return self.question_text


# Options Model
class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.option_text
    
class QuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()
    total = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title}"

# Weekly Progress Chart 
# --- Naya Model Chart ke liye (Daily Learning Hours) ---
class DailyLearning(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    hours = models.FloatField(default=0.0)

    class Meta:
        unique_together = ('user', 'date')

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.hours}h"