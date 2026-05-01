# Generated manually for independent instructor profile courses

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Page', '0006_top_courses_instructor_instructorreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstructorCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_image', models.FileField(blank=True, default=None, max_length=250, null=True, upload_to='courses/')),
                ('course_title', models.CharField(max_length=150)),
                ('course_des', models.TextField(blank=True)),
                ('course_duration', models.CharField(blank=True, max_length=55)),
                ('course_level', models.CharField(blank=True, max_length=55)),
                ('course_price', models.CharField(blank=True, max_length=100)),
                ('display_order', models.PositiveIntegerField(default=0)),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_courses', to='Home_Page.instructor')),
            ],
            options={
                'ordering': ['display_order', 'id'],
            },
        ),
        migrations.RemoveField(
            model_name='top_courses',
            name='instructor',
        ),
    ]
