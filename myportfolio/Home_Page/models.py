from django.db import models

# Create your models here.
class Logo(models.Model):
    favicon = models.ImageField(upload_to='favicon/', default=None, null=True)
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
    # instruct_skill = models.CharField(max_length=55)
    # about_instruct = models.TextField()
    def __str__(self):
        return self.instruct_name


class InstructorDetail(models.Model):
    instructor = models.OneToOneField(Instructor, on_delete=models.CASCADE, related_name='detail')
    title = models.CharField(max_length=150, blank=True)
    experience = models.CharField(max_length=80, blank=True)
    rating = models.CharField(max_length=20, blank=True)
    students = models.CharField(max_length=50, blank=True)
    courses_count = models.CharField(max_length=30, blank=True)
    about = models.TextField(blank=True)
    skills = models.CharField(max_length=300, blank=True, help_text='Example: Python, Django, React')
    project_title_1 = models.CharField(max_length=150, blank=True)
    project_des_1 = models.TextField(blank=True)
    project_link_1 = models.URLField(blank=True)
    project_title_2 = models.CharField(max_length=150, blank=True)
    project_des_2 = models.TextField(blank=True)
    project_link_2 = models.URLField(blank=True)
    qualification_1 = models.CharField(max_length=200, blank=True)
    qualification_from_1 = models.CharField(max_length=150, blank=True)
    qualification_2 = models.CharField(max_length=200, blank=True)
    qualification_from_2 = models.CharField(max_length=150, blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    facebook = models.URLField(blank=True)

    def __str__(self):
        return f"{self.instructor.instruct_name} Detail"

class Top_Courses(models.Model):
       instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True, blank=True, related_name='top_course_details')
       course_image = models.FileField(upload_to='courses/',max_length=250,null=True, default=None)
       course_title = models.CharField(max_length=150)
       course_des =models.TextField(blank=True, default='')
       course_duration = models.CharField(max_length=55)
       course_price = models.CharField(max_length=100)
       course_level = models.CharField(max_length=55, blank=True, default='')
       course_lessons = models.CharField(max_length=55, blank=True, default='')
       course_language = models.CharField(max_length=55, blank=True, default='English / Urdu')
       course_outline = models.TextField(blank=True, default='', help_text='Write each outline point on a new line.')
       course_requirements = models.TextField(blank=True, default='', help_text='Write each requirement on a new line.')
       course_projects = models.TextField(blank=True, default='', help_text='Write each project/practice item on a new line.')
       course_outcomes = models.TextField(blank=True, default='', help_text='Write each learning outcome on a new line.')
       course_certificate = models.CharField(max_length=150, blank=True, default='Certificate guidance')
       course_support = models.CharField(max_length=150, blank=True, default='Student support')
       course_enroll_note = models.TextField(blank=True, default='Enroll to continue with this course and begin learning with Smart Learn LMS.')
       def __str__(self):
              return self.course_title


class InstructorCourse(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='profile_courses')
    course_image = models.FileField(upload_to='courses/', max_length=250, null=True, blank=True, default=None)
    course_title = models.CharField(max_length=150)
    course_des = models.TextField(blank=True)
    course_duration = models.CharField(max_length=55, blank=True)
    course_level = models.CharField(max_length=55, blank=True)
    course_price = models.CharField(max_length=100, blank=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order', 'id']

    def __str__(self):
        return f"{self.instructor.instruct_name} - {self.course_title}"


class InstructorReview(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='reviews')
    student_name = models.CharField(max_length=100)
    student_image = models.ImageField(upload_to='testimonial/', default='default/user.png', blank=True, null=True)
    rating = models.PositiveSmallIntegerField(default=5)
    review_text = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.student_name} - {self.instructor.instruct_name}"


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
