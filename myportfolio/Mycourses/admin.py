from django.contrib import admin
from Mycourses.models import myCourses


@admin.register(myCourses)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_title', 'course_des', 'course_level', 'course_duration', 'course_image')
    search_fields = ('course_title', 'course_des', 'course_level', 'course_duration')
    list_filter = ('course_level', 'course_duration')
