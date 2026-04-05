from django.contrib import admin
from Home_Page.models import (
    Logo,
    FounderMessage,
    Feature,
    Instructor,
    Top_Courses,
    FooterSettings,
    FooterLink,
    FooterContact,
    FooterSocialLink,
)


@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('nav_title', 'nav_logo')
    search_fields = ('nav_title',)


@admin.register(FounderMessage)
class FounderMessageAdmin(admin.ModelAdmin):
    list_display = ('message_title', 'founder_name', 'visit_founder')
    search_fields = ('message_title', 'founder_name', 'founder_message')


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('feature_title', 'feature_icon')
    search_fields = ('feature_title', 'feature_des', 'feature_icon')


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('instruct_name', 'instruct_skill', 'instruct_img')
    search_fields = ('instruct_name', 'instruct_skill', 'about_instruct')


@admin.register(Top_Courses)
class TopCoursesAdmin(admin.ModelAdmin):
    list_display = ('course_title', 'course_duration', 'course_price')
    search_fields = ('course_title', 'course_des', 'course_duration', 'course_price')


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
