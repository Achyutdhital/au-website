# Generated by Django 4.2.7 on 2023-12-05 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_organizationchart_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='linkedin_link',
        ),
        migrations.RemoveField(
            model_name='team',
            name='twitter_link',
        ),
    ]
