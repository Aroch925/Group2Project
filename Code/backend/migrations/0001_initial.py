# Generated by Django 2.0.4 on 2018-04-22 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(help_text='Enter User Name', max_length=20)),
                ('password', models.CharField(help_text='Enter a password', max_length=20)),
                ('first', models.CharField(help_text='Enter your first Name', max_length=20)),
                ('last', models.CharField(help_text='Enter your last name', max_length=20)),
            ],
        ),
    ]