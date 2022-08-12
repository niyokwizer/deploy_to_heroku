# Generated by Django 4.0.6 on 2022-08-03 01:23

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_rename_userregistrationform_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('released_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('main_actor', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('descripltion', models.CharField(max_length=255)),
                ('video', models.FileField(null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('thumbnail', models.ImageField(upload_to='thumbnail')),
            ],
        ),
    ]
