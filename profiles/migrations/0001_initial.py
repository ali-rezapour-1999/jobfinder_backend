# Generated by Django 5.1.3 on 2024-11-14 11:33

import core.utils
import profiles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(max_length=200)),
                ('degree', models.CharField(max_length=200)),
                ('field_of_study', models.CharField(blank=True, max_length=200, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug_id', models.CharField(default=core.utils.generate_unique_id, max_length=8, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('nickname', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('phone_number', models.CharField(max_length=11, unique=True, validators=[profiles.models.validate_iranian_phone_number])),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('address', models.TextField(blank=True, null=True)),
                ('description_myself', models.TextField(blank=True, null=True)),
                ('cv_file', models.FileField(blank=True, null=True, upload_to='cv_files/')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('telegram', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('github', models.URLField(blank=True, null=True)),
                ('gitlab', models.URLField(blank=True, null=True)),
                ('gitbe', models.URLField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(blank=True, max_length=200)),
                ('company_name', models.CharField(blank=True, max_length=200)),
                ('start_date', models.DateField(blank=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('job_description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
