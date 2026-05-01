# Generated manually for instructor detail page

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Page', '0003_logo_favicon'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstructorDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150)),
                ('experience', models.CharField(blank=True, max_length=80)),
                ('rating', models.CharField(blank=True, max_length=20)),
                ('students', models.CharField(blank=True, max_length=50)),
                ('courses_count', models.CharField(blank=True, max_length=30)),
                ('about', models.TextField(blank=True)),
                ('skills', models.CharField(blank=True, help_text='Example: Python, Django, React', max_length=300)),
                ('project_title_1', models.CharField(blank=True, max_length=150)),
                ('project_des_1', models.TextField(blank=True)),
                ('project_link_1', models.URLField(blank=True)),
                ('project_title_2', models.CharField(blank=True, max_length=150)),
                ('project_des_2', models.TextField(blank=True)),
                ('project_link_2', models.URLField(blank=True)),
                ('qualification_1', models.CharField(blank=True, max_length=200)),
                ('qualification_from_1', models.CharField(blank=True, max_length=150)),
                ('qualification_2', models.CharField(blank=True, max_length=200)),
                ('qualification_from_2', models.CharField(blank=True, max_length=150)),
                ('linkedin', models.URLField(blank=True)),
                ('github', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('facebook', models.URLField(blank=True)),
                ('instructor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='Home_Page.instructor')),
            ],
        ),
    ]
