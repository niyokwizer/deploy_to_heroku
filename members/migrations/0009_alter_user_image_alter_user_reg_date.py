# Generated by Django 4.0.6 on 2022-08-05 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_alter_movies_released_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(null=True, upload_to='profile'),
        ),
        migrations.AlterField(
            model_name='user',
            name='reg_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
