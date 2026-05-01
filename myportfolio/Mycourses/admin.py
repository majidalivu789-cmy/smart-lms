from django.contrib import admin
from Mycourses.models import myCourses


@admin.register(myCourses)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_title', 'instructor', 'course_level', 'course_duration', 'course_price', 'course_image')
    search_fields = ('course_title', 'course_des', 'course_level', 'course_duration', 'course_price', 'instructor__instruct_name')
    list_filter = ('instructor', 'course_level', 'course_duration')
    fieldsets = (
        ('Basic Course Info', {
            'fields': ('instructor', 'course_title', 'course_image', 'course_des', 'course_level', 'course_duration', 'course_price')
        }),
        ('Professional Detail Page Content', {
            'fields': (
                'course_lessons',
                'course_language',
                'course_outline',
                'course_outcomes',
                'course_requirements',
                'course_projects',
                'course_certificate',
                'course_support',
                'course_enroll_note',
            )
        }),
    )
