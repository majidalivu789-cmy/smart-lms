from django.contrib import admin
from About_Page.models import AboutSml, AboutFeature, StudentReview


@admin.register(AboutSml)
class AboutSmlAdmin(admin.ModelAdmin):
    list_display = ('about_title',)
    search_fields = ('about_title', 'about_des')


@admin.register(AboutFeature)
class AboutFeatureAdmin(admin.ModelAdmin):
    list_display = ('feature_title', 'feature_user', 'feature_icon')
    search_fields = ('feature_title', 'feature_user', 'feature_icon')


@admin.register(StudentReview)
class StudentReviewAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'student_role', 'rating', 'display_order', 'is_active', 'created_at')
    list_filter = ('is_active', 'rating', 'created_at')
    search_fields = ('student_name', 'student_role', 'review_text')
    date_hierarchy = 'created_at'
