# Generated manually to keep dashboard courses separate from instructor profiles

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard_Page', '0006_dashboardcourse_instructor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboardcourse',
            name='instructor',
        ),
    ]
