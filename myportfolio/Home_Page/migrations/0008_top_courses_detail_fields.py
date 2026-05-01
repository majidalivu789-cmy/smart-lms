# Generated manually for professional top course detail pages

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Page', '0007_instructorcourse_remove_top_course_instructor'),
    ]

    operations = [
        migrations.AddField(
            model_name='top_courses',
            name='course_level',
            field=models.CharField(blank=True, default='', max_length=55),
        ),
        migrations.AddField(
            model_name='top_courses',
            name='course_lessons',
            field=models.CharField(blank=True, default='', max_length=55),
        ),
        migrations.AddField(
            model_name='top_courses',
            name='course_language',
            field=models.CharField(blank=True, default='English / Urdu', max_length=55),
        ),
        migrations.AddField(
            model_name='top_courses',
            name='course_outline',
            field=models.TextField(blank=True, default='', help_text='Write each outline point on a new line.'),
        ),
        migrations.AddField(
            model_name='top_courses',
            name='course_requirements',
            field=models.TextField(blank=True, default='', help_text='Write each requirement on a new line.'),
        ),
        migrations.AddField(
            model_name='top_courses',
            name='course_projects',
            field=models.TextField(blank=True, default='', help_text='Write each project/practice item on a new line.'),
        ),
    ]
