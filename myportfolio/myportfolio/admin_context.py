import json
from collections import OrderedDict
from decimal import Decimal, InvalidOperation
from datetime import timedelta

from django.contrib.auth.models import User
from django.utils import timezone

from About_Page.models import StudentReview
from Contact_Page.models import ContactMessage
from Dashboard_Page.models import DashboardCourse, Enrollment
from Home_Page.models import Instructor


def parse_course_fee(fee_value):
    """
    Convert fee text like 'Rs. 25,000' into a number for admin insights.
    """
    cleaned_value = ''.join(ch for ch in str(fee_value or '') if ch.isdigit() or ch == '.')
    if not cleaned_value:
        return Decimal('0')

    try:
        return Decimal(cleaned_value)
    except InvalidOperation:
        return Decimal('0')


def admin_dashboard_stats(request):
    """
    Add LMS totals and chart data to the existing Django admin homepage.
    """
    if not request.path.startswith('/admin/'):
        return {}

    total_students = User.objects.filter(is_staff=False, is_superuser=False).count()
    total_courses = DashboardCourse.objects.count()
    total_enrollments = Enrollment.objects.count()
    total_instructors = Instructor.objects.count()
    total_reviews = StudentReview.objects.filter(is_active=True).count()
    total_messages = ContactMessage.objects.count()

    paid_enrollments = Enrollment.objects.filter(is_paid=True).select_related('course')
    total_earnings = Decimal('0')
    for enrollment in paid_enrollments:
        total_earnings += parse_course_fee(enrollment.course.course_fees)

    # Last 6 months of student registrations.
    today = timezone.now()
    student_growth = OrderedDict()
    for month_offset in range(5, -1, -1):
        month_number = today.month - month_offset
        year_number = today.year

        while month_number <= 0:
            month_number += 12
            year_number -= 1

        current_month = today.replace(year=year_number, month=month_number, day=1)
        student_growth[current_month.strftime('%b %Y')] = 0

    recent_students = User.objects.filter(
        is_staff=False,
        is_superuser=False,
        date_joined__gte=today - timedelta(days=180)
    )
    for student in recent_students:
        month_key = student.date_joined.strftime('%b %Y')
        if month_key in student_growth:
            student_growth[month_key] += 1

    # Last 6 months of paid enrollments as earnings.
    earnings_growth = OrderedDict((label, 0.0) for label in student_growth.keys())
    for enrollment in paid_enrollments:
        month_key = enrollment.enrolled_at.strftime('%b %Y')
        if month_key in earnings_growth:
            earnings_growth[month_key] += float(parse_course_fee(enrollment.course.course_fees))

    course_popularity = []
    for course in DashboardCourse.objects.all():
        popularity_count = Enrollment.objects.filter(course=course, is_paid=True).count()
        if popularity_count:
            course_popularity.append({
                'label': course.course_title,
                'value': popularity_count,
            })

    course_popularity = sorted(course_popularity, key=lambda item: item['value'], reverse=True)[:5]

    return {
        'admin_total_students': total_students,
        'admin_total_courses': total_courses,
        'admin_total_enrollments': total_enrollments,
        'admin_total_earnings': total_earnings,
        'admin_total_instructors': total_instructors,
        'admin_total_reviews': total_reviews,
        'admin_total_messages': total_messages,
        'admin_student_growth_labels': json.dumps(list(student_growth.keys())),
        'admin_student_growth_values': json.dumps(list(student_growth.values())),
        'admin_earnings_labels': json.dumps(list(earnings_growth.keys())),
        'admin_earnings_values': json.dumps(list(earnings_growth.values())),
        'admin_popularity_labels': json.dumps([item['label'] for item in course_popularity]),
        'admin_popularity_values': json.dumps([item['value'] for item in course_popularity]),
    }
