# Generated by Django 4.2.7 on 2023-12-06 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_sliderimg'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sliderimg',
            options={'ordering': ['-id']},
        ),
    ]
