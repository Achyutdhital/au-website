# Generated by Django 4.2.7 on 2023-12-06 04:50

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_team_linkedin_link_remove_team_twitter_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, populate_from='name', unique=True),
        ),
    ]
