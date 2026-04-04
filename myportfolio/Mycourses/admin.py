from django.contrib import admin
from Mycourses.models import myCourses
class courseAdmin(admin.ModelAdmin):
    list_display = ('course_title','course_des','course_image','course_level','course_duration')
admin.site.register(myCourses,courseAdmin)

# Register your models here.
