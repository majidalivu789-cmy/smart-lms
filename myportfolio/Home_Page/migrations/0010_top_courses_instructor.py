# Generated manually to show instructor on top course detail pages

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Page', '0009_alter_top_courses_course_des'),
    ]

    operations = [
        migrations.AddField(
            model_name='top_courses',
            name='instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='top_course_details', to='Home_Page.instructor'),
        ),
    ]
