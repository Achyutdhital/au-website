# Generated by Django 4.2.7 on 2023-12-06 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_testimonial_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='representinstitute',
            name='link',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]