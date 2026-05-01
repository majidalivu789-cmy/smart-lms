# Generated manually to make top course description optional

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Page', '0008_top_courses_detail_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='top_courses',
            name='course_des',
            field=models.TextField(blank=True, default=''),
        ),
    ]
