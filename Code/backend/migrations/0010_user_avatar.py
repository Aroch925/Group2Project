# Generated by Django 2.0.4 on 2018-05-08 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_remove_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.FileField(default='profile-placeholder.png', upload_to=''),
        ),
    ]
