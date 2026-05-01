# Generated manually to keep public courses separate from instructor profiles

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mycourses', '0004_mycourses_instructor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mycourses',
            name='instructor',
        ),
    ]
