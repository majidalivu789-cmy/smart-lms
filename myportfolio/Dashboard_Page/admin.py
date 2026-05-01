from django.contrib import admin
from .models import (
    DashboardCourse,
    ProfileImage,
    Student,
    CourseWeek,
    CourseLecture,
    Enrollment,
    Updates,
    ImportantLinks,
    VideoProgress,
    Quiz,
    Question,
    Option,
    QuizResult,
    DailyLearning,
)


class CourseWeekInline(admin.TabularInline):
    model = CourseWeek
    extra = 1


@admin.register(DashboardCourse)
class DashboardCourseAdmin(admin.ModelAdmin):
    list_display = ('course_title', 'instructor', 'course_level', 'course_duration', 'course_fees', 'total_weeks', 'total_enrollments', 'paid_enrollments')
    search_fields = ('course_title', 'course_fees', 'course_icon', 'course_des', 'instructor__instruct_name')
    list_filter = ('instructor', 'course_level', 'course_duration')
    fieldsets = (
        ('Basic Course Info', {
            'fields': ('instructor', 'course_icon', 'course_image', 'course_title', 'course_des', 'course_level', 'course_duration', 'course_fees')
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
    inlines = [CourseWeekInline]

    def total_weeks(self, obj):
        return obj.weeks.count()
    total_weeks.short_description = 'Weeks'

    def total_enrollments(self, obj):
        return obj.enrollment_set.count()
    total_enrollments.short_description = 'Enrollments'

    def paid_enrollments(self, obj):
        return obj.enrollment_set.filter(is_paid=True).count()
    paid_enrollments.short_description = 'Paid Enrollments'


@admin.register(ProfileImage)
class ProfileImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'cnic', 'gender', 'phone', 'district', 'education')
    search_fields = ('name', 'cnic', 'phone', 'district', 'address')
    list_filter = ('gender', 'province', 'education', 'country')


@admin.register(CourseWeek)
class CourseWeekAdmin(admin.ModelAdmin):
    list_display = ('course', 'week_number', 'lecture_count')
    search_fields = ('course__course_title',)
    list_filter = ('course',)

    def lecture_count(self, obj):
        return obj.lectures.count()
    lecture_count.short_description = 'Lectures'


@admin.register(CourseLecture)
class CourseLectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'week', 'course_title')
    search_fields = ('title', 'week__course__course_title')
    list_filter = ('week__course', 'week')

    def course_title(self, obj):
        return obj.week.course.course_title
    course_title.short_description = 'Course'


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_email', 'course', 'is_paid', 'course_fee', 'enrolled_at')
    search_fields = ('user__username', 'user__email', 'course__course_title')
    list_filter = ('is_paid', 'enrolled_at', 'course')
    autocomplete_fields = ('user', 'course')
    date_hierarchy = 'enrolled_at'

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = 'Email'

    def course_fee(self, obj):
        return obj.course.course_fees
    course_fee.short_description = 'Fee'


@admin.register(Updates)
class UpdatesAdmin(admin.ModelAdmin):
    list_display = ('updation_title', 'updation_tag', 'button_type', 'updation_date')
    search_fields = ('updation_title', 'updation_desc', 'button_link')
    list_filter = ('updation_tag', 'button_type', 'updation_date')
    date_hierarchy = 'updation_date'


@admin.register(ImportantLinks)
class ImportantLinksAdmin(admin.ModelAdmin):
    list_display = ('link_title', 'link_icon', 'is_new', 'created_at')
    search_fields = ('link_title', 'link_desc', 'important_link')
    list_filter = ('is_new', 'created_at', 'link_icon')
    date_hierarchy = 'created_at'


@admin.register(VideoProgress)
class VideoProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'lecture', 'watched', 'course_name')
    search_fields = ('user__username', 'user__email', 'lecture__title', 'lecture__week__course__course_title')
    list_filter = ('watched', 'lecture__week__course')
    autocomplete_fields = ('user', 'lecture')

    def course_name(self, obj):
        return obj.lecture.week.course.course_title
    course_name.short_description = 'Course'


class OptionInline(admin.TabularInline):
    model = Option
    extra = 4


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'total_questions', 'time', 'start_date', 'expiry_date')
    search_fields = ('title', 'course__course_title', 'icon')
    list_filter = ('course', 'start_date', 'expiry_date')
    date_hierarchy = 'start_date'


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'quiz', 'course_name')
    search_fields = ('question_text', 'quiz__title', 'quiz__course__course_title')
    list_filter = ('quiz', 'quiz__course')
    inlines = [OptionInline]

    def course_name(self, obj):
        return obj.quiz.course
    course_name.short_description = 'Course'


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('option_text', 'question', 'is_correct')
    search_fields = ('option_text', 'question__question_text', 'question__quiz__title')
    list_filter = ('is_correct', 'question__quiz')


@admin.register(QuizResult)
class QuizResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'score', 'total', 'created_at')
    search_fields = ('user__username', 'user__email', 'quiz__title')
    list_filter = ('quiz', 'created_at')
    date_hierarchy = 'created_at'
    autocomplete_fields = ('user', 'quiz')


@admin.register(DailyLearning)
class DailyLearningAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'hours')
    search_fields = ('user__username', 'user__email')
    list_filter = ('date',)
    date_hierarchy = 'date'
    autocomplete_fields = ('user',)
