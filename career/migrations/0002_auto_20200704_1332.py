# Generated by Django 3.0.8 on 2020-07-04 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='dateofissue',
            field=models.DateField(auto_now_add=True),
        ),
    ]
