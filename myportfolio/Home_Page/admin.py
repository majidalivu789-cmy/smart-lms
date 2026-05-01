from django.contrib import admin
from Home_Page.models import (
    Logo,
    FounderMessage,
    Feature,
    Instructor,
    InstructorCourse,
    InstructorDetail,
    InstructorReview,
    Top_Courses,
    FooterSettings,
    FooterLink,
    FooterContact,
    FooterSocialLink,
)


@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('nav_title', 'nav_logo', 'favicon')
    search_fields = ('nav_title',)


@admin.register(FounderMessage)
class FounderMessageAdmin(admin.ModelAdmin):
    list_display = ('message_title', 'founder_name', 'visit_founder')
    search_fields = ('message_title', 'founder_name', 'founder_message')


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('feature_title', 'feature_icon')
    search_fields = ('feature_title', 'feature_des', 'feature_icon')


class InstructorDetailInline(admin.StackedInline):
    model = InstructorDetail
    extra = 0
    max_num = 1
    can_delete = False
    verbose_name = 'Instructor Detail'
    verbose_name_plural = 'Instructor Detail - yahan se isi instructor ki detail add karein'
    fields = (
        'title',
        'experience',
        'rating',
        'students',
        'courses_count',
        'about',
        'skills',
        'project_title_1',
        'project_des_1',
        'project_link_1',
        'project_title_2',
        'project_des_2',
        'project_link_2',
        'qualification_1',
        'qualification_from_1',
        'qualification_2',
        'qualification_from_2',
        'linkedin',
        'github',
        'twitter',
        'facebook',
    )


class InstructorCourseInline(admin.TabularInline):
    model = InstructorCourse
    extra = 0
    fields = ('course_title', 'course_image', 'course_des', 'course_duration', 'course_level', 'course_price', 'display_order')
    verbose_name = 'Instructor Course'
    verbose_name_plural = 'Instructor Courses - add only the courses this instructor teaches'


class InstructorReviewInline(admin.TabularInline):
    model = InstructorReview
    extra = 0
    fields = ('student_name', 'student_image', 'rating', 'review_text', 'is_active')
    verbose_name = 'Instructor Review'
    verbose_name_plural = 'Reviews - yahan se isi instructor ke reviews add karein'


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('instruct_name','instruct_img')
    search_fields = ('instruct_name',)
    inlines = (InstructorDetailInline, InstructorCourseInline, InstructorReviewInline)


@admin.register(InstructorDetail)
class InstructorDetailAdmin(admin.ModelAdmin):
    list_display = ('instructor', 'title', 'experience', 'rating')
    list_filter = ('instructor',)
    search_fields = ('instructor__instruct_name', 'title', 'about', 'skills')
    fields = (
        'instructor',
        'title',
        'experience',
        'rating',
        'students',
        'courses_count',
        'about',
        'skills',
        'project_title_1',
        'project_des_1',
        'project_link_1',
        'project_title_2',
        'project_des_2',
        'project_link_2',
        'qualification_1',
        'qualification_from_1',
        'qualification_2',
        'qualification_from_2',
        'linkedin',
        'github',
        'twitter',
        'facebook',
    )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        formfield = super().formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == 'instructor':
            formfield.label = 'Select Instructor From Home Page List'
            formfield.help_text = 'First select an instructor from here, then add the instructor detail below.'
        return formfield


@admin.register(Top_Courses)
class TopCoursesAdmin(admin.ModelAdmin):
    list_display = ('course_title', 'instructor', 'course_level', 'course_duration', 'course_price')
    list_filter = ('instructor', 'course_level')
    search_fields = ('course_title', 'course_des', 'course_duration', 'course_price', 'course_level', 'instructor__instruct_name')
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


@admin.register(InstructorCourse)
class InstructorCourseAdmin(admin.ModelAdmin):
    list_display = ('course_title', 'instructor', 'course_duration', 'course_level', 'course_price', 'display_order')
    list_filter = ('instructor', 'course_level')
    search_fields = ('course_title', 'course_des', 'instructor__instruct_name')


@admin.register(InstructorReview)
class InstructorReviewAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'instructor', 'rating', 'is_active', 'created_at')
    list_filter = ('instructor', 'rating', 'is_active')
    search_fields = ('student_name', 'review_text', 'instructor__instruct_name')


@admin.register(FooterSettings)
class FooterSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'newsletter_button_text')
    search_fields = ('site_name', 'copyright_text')


@admin.register(FooterLink)
class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ('label', 'section', 'display_order', 'is_active')
    list_filter = ('section', 'is_active')
    search_fields = ('label', 'url')


@admin.register(FooterContact)
class FooterContactAdmin(admin.ModelAdmin):
    list_display = ('value', 'display_order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('value',)


@admin.register(FooterSocialLink)
class FooterSocialLinkAdmin(admin.ModelAdmin):
    list_display = ('platform', 'display_order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('platform', 'url')
