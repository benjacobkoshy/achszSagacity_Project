# Generated by Django 5.0.1 on 2024-06-19 06:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(null=True, upload_to='images/user_image/')),
                ('address', models.TextField()),
                ('place', models.CharField(max_length=30)),
                ('pin', models.CharField(max_length=10)),
                ('dob', models.DateField(null=True)),
                ('deleted_status', models.IntegerField(choices=[(0, 'Live'), (0, 'Delete')], default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
