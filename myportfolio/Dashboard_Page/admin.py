from django.contrib import admin
from .models import*
# Register your models here.
admin.site.register(DashboardCourse)
admin.site.register(Enrollment)

@admin.register(CourseWeek)
class CourseWeekAdmin(admin.ModelAdmin):
    list_display = ('course', 'week_number')
    list_filter = ('course',)


@admin.register(CourseLecture)
class CourseLectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'week')
    list_filter = ('week__course', 'week')

# ===== News and Events Page ====
admin.site.register(Updates)
# ==== Important Links ======
admin.site.register(ImportantLinks)

# ====== Quiz Page =======
# 👇 Option inline (ye magic hai)
class OptionInline(admin.TabularInline):
    model = Option
    extra = 4   # 👈 4 empty option boxes automatically

# 👇 Question admin
class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]

# Register models
admin.site.register(Quiz)
admin.site.register(Question, QuestionAdmin)
