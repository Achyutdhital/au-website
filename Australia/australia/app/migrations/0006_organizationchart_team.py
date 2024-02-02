# Generated by Django 4.2.7 on 2023-12-05 10:44

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_event_event_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationChart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('org_slug', autoslug.fields.AutoSlugField(default=None, editable=False, populate_from='name', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('team_member_photo', models.ImageField(upload_to='team')),
                ('member_designation', models.CharField(max_length=100)),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('twitter_link', models.URLField(blank=True, null=True)),
                ('linkedin_link', models.URLField(blank=True, null=True)),
                ('instagram_link', models.URLField(blank=True, null=True)),
                ('organizationChart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organizationChart', to='app.organizationchart')),
            ],
        ),
    ]