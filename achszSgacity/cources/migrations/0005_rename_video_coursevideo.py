# Generated by Django 5.0.1 on 2024-06-25 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cources', '0004_coursematerial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Video',
            new_name='CourseVideo',
        ),
    ]
