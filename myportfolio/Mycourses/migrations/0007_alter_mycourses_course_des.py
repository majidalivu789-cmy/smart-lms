# Generated manually to make public course description optional

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mycourses', '0006_mycourses_detail_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycourses',
            name='course_des',
            field=models.TextField(blank=True, default=''),
        ),
    ]
