# Generated by Django 4.0.6 on 2022-08-03 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_alter_movies_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='released_date',
            field=models.CharField(max_length=255),
        ),
    ]
