# Generated by Django 4.2.7 on 2023-12-07 15:48

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_alter_breadcrumb_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programs',
            name='program_slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, populate_from='description', unique=True),
        ),
    ]