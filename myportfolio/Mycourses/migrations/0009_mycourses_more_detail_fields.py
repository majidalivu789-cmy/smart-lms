# Generated manually to make public course detail page content fully dynamic

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mycourses', '0008_mycourses_instructor'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycourses',
            name='course_outcomes',
            field=models.TextField(blank=True, default='', help_text='Write each learning outcome on a new line.'),
        ),
        migrations.AddField(
            model_name='mycourses',
            name='course_certificate',
            field=models.CharField(blank=True, default='Certificate guidance', max_length=150),
        ),
        migrations.AddField(
            model_name='mycourses',
            name='course_support',
            field=models.CharField(blank=True, default='Student support', max_length=150),
        ),
        migrations.AddField(
            model_name='mycourses',
            name='course_enroll_note',
            field=models.TextField(blank=True, default='Enroll to continue with this course and begin learning with Smart Learn LMS.'),
        ),
    ]
