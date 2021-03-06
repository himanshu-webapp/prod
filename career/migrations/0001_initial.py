# Generated by Django 3.0.8 on 2020-07-04 08:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ssn', models.CharField(default='000', max_length=200)),
                ('certificateno', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200, null=True)),
                ('authorizationcode', models.CharField(max_length=200, null=True)),
                ('role', models.CharField(max_length=200, null=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=50)),
                ('dateofissue', models.DateField(default=datetime.datetime(2020, 7, 4, 8, 1, 32, 409326, tzinfo=utc))),
                ('dateofexpiry', models.DateField(blank=True, null=True)),
                ('certificate', models.FileField(upload_to='certificates/%Y/%m/%d/')),
            ],
            options={
                'ordering': ['dateofissue'],
            },
        ),
        migrations.CreateModel(
            name='InternshipApplication',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('college', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=100)),
                ('profile_applying_for', models.CharField(blank=True, max_length=200, null=True)),
                ('tenth_Percent', models.CharField(max_length=100)),
                ('twelfth_Percent', models.CharField(max_length=100)),
                ('Graduation_Percent', models.CharField(max_length=100)),
                ('date_applied', models.DateTimeField(default=django.utils.timezone.now)),
                ('duration_in_weeks', models.CharField(max_length=10, null=True)),
                ('available_from', models.DateField(null=True)),
                ('available_to', models.DateField(blank=True, null=True)),
                ('skills', models.TextField(blank=True, null=True)),
                ('other_description', models.TextField(blank=True, null=True)),
                ('linkedin_profile_link', models.URLField(blank=True, max_length=500, null=True)),
                ('resume', models.FileField(upload_to='uploads/intern-application')),
                ('experience', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('college', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=100)),
                ('profile_applying_for', models.CharField(max_length=100)),
                ('tenth_Percent', models.CharField(max_length=100)),
                ('twelfth_Percent', models.CharField(max_length=100)),
                ('Graduation_Percent', models.CharField(max_length=100)),
                ('experience', models.CharField(blank=True, max_length=20, null=True)),
                ('current_CTC', models.CharField(blank=True, max_length=20, null=True)),
                ('expected_CTC', models.CharField(blank=True, max_length=20, null=True)),
                ('location_city', models.CharField(max_length=50, null=True)),
                ('location_state', models.CharField(max_length=50, null=True)),
                ('skills', models.TextField(null=True)),
                ('present_workplace', models.CharField(blank=True, max_length=200, null=True)),
                ('current_position', models.CharField(blank=True, max_length=100, null=True)),
                ('other_description', models.TextField(blank=True, null=True)),
                ('availablity_date', models.DateField(null=True)),
                ('linkedin_profile_link', models.URLField(blank=True, max_length=500, null=True)),
                ('resume', models.FileField(upload_to='uploads/job-application')),
                ('date_applied', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
