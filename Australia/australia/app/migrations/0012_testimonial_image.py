# Generated by Django 4.2.7 on 2023-12-06 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_company_info_representinstitute_testimonial_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(default=1, upload_to='testimonial/'),
            preserve_default=False,
        ),
    ]