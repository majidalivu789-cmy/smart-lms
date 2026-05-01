# Generated manually for linking dashboard courses to instructors

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Page', '0006_top_courses_instructor_instructorreview'),
        ('Dashboard_Page', '0005_dailylearning'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboardcourse',
            name='instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dashboard_courses', to='Home_Page.instructor'),
        ),
    ]
