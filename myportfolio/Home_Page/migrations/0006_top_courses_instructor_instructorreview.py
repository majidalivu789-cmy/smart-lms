# Generated manually for instructor courses and reviews

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Page', '0005_remove_old_instructor_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='top_courses',
            name='instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='courses', to='Home_Page.instructor'),
        ),
        migrations.CreateModel(
            name='InstructorReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('student_image', models.ImageField(blank=True, default='default/user.png', null=True, upload_to='testimonial/')),
                ('rating', models.PositiveSmallIntegerField(default=5)),
                ('review_text', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='Home_Page.instructor')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
