# Generated by Django 5.0.1 on 2024-06-24 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cources', '0002_course_course_image_course_description_course_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='detailed_name',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
    ]
