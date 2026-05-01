# Generated manually to match the current Instructor model

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Page', '0004_instructordetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='about_instruct',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='instruct_skill',
        ),
    ]
