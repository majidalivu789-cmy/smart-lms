# Generated manually for professional public course detail pages

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mycourses', '0005_remove_mycourses_instructor'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycourses',
            name='course_price',
            field=models.CharField(blank=True, default='Free', max_length=100),
        ),
        migrations.AddField(
            model_name='mycourses',
            name='course_lessons',
            field=models.CharField(blank=True, default='', max_length=55),
        ),
        migrations.AddField(
            model_name='mycourses',
            name='course_language',
            field=models.CharField(blank=True, default='English / Urdu', max_length=55),
        ),
        migrations.AddField(
            model_name='mycourses',
            name='course_outline',
            field=models.TextField(blank=True, default='', help_text='Write each outline point on a new line.'),
        ),
        migrations.AddField(
            model_name='mycourses',
            name='course_requirements',
            field=models.TextField(blank=True, default='', help_text='Write each requirement on a new line.'),
        ),
        migrations.AddField(
            model_name='mycourses',
            name='course_projects',
            field=models.TextField(blank=True, default='', help_text='Write each project/practice item on a new line.'),
        ),
    ]
