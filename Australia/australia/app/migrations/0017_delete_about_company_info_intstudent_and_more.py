# Generated by Django 4.2.7 on 2023-12-07 05:24

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_company_info_logo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='About',
        ),
        migrations.AddField(
            model_name='company_info',
            name='intStudent',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company_info',
            name='representInstitute',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company_info',
            name='scholarshipApproved',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company_info',
            name='studentEnrolled',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company_info',
            name='description',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company_info',
            name='location_link',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='company_info',
            name='youtube_link',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]