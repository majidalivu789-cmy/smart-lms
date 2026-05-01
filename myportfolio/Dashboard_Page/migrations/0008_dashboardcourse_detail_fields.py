# Generated manually to make dashboard course detail pages dynamic

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Page', '0011_top_courses_more_detail_fields'),
        ('Dashboard_Page', '0007_remove_dashboardcourse_instructor'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboardcourse',
            name='instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dashboard_course_details', to='Home_Page.instructor'),
        ),
        migrations.AddField(
            model_name='dashboardcourse',
            name='course_image',
            field=models.FileField(blank=True, default=None, max_length=250, null=True, upload_to='courses/'),
        ),
        migrations.AddField(
            model_name='dashboardcourse',
            name='course_des',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='dashboardcourse',
            name='course_level',
            field=models.CharField(blank=True, default='Beginner', max_length=55),
        ),
        migrations.AddField(
            model_name='dashboardcourse',
            name='course_duration',
            field=models.CharField(blank=True, default='Flexible', max_length=55),
        ),
        migrations.AddField(
            model_name='dashboardcourse',
            name='course_lessons',
            field=models.CharField(blank=True, default='', max_length=55),
        ),
        migrations.AddField(
            model_name='dashboardcourse',
            name='course_language',
            field=models.CharField(blank=True, default='English / Urdu', max_length=55),
        ),
        migrations.AddField(
            model_name='dashboardcourse',
            name='course_outline',
            field=models.TextField(blank=True, default='', help_text='Write each outline point on a new line.'),
        ),
        migrations.AddField(
            model_name='dashboardcourse',
            name='course_outcomes',
            field=models.TextField(blank=True, default='', help_text='Write each learning outcome on a new line.'),
        ),
        migrations.AddField(
            model_name='dashboardcourse',
            name='course_requirements',
            field=models.TextField(blank=True, default='', help_text='Write each requirement on a new line.'),
        ),
        migrations.AddField(
            model_name='dashboardcourse',
            name='course_projects',
            field=models.TextField(blank=True, default='', help_text='Write each project/practice item on a new line.'),
        ),
        migrations.AddField(
            model_name='dashboardcourse',
            name='course_certificate',
            field=models.CharField(blank=True, default='Certificate after completion', max_length=150),
        ),
        migrations.AddField(
            model_name='dashboardcourse',
            name='course_support',
            field=models.CharField(blank=True, default='Student support', max_length=150),
        ),
        migrations.AddField(
            model_name='dashboardcourse',
            name='course_enroll_note',
            field=models.TextField(blank=True, default='Please confirm before enrolling. This course will be unlocked on your dashboard after enrollment.'),
        ),
    ]
