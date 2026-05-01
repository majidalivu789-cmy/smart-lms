# Generated manually to show instructor on public course detail pages

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Page', '0010_top_courses_instructor'),
        ('Mycourses', '0007_alter_mycourses_course_des'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycourses',
            name='instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='public_course_details', to='Home_Page.instructor'),
        ),
    ]
