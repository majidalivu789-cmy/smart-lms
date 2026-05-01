# Generated manually for linking public courses to instructors

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Page', '0006_top_courses_instructor_instructorreview'),
        ('Mycourses', '0003_mycourses_course_duration_mycourses_course_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycourses',
            name='instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='public_courses', to='Home_Page.instructor'),
        ),
    ]
