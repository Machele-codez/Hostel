# Generated by Django 2.2.7 on 2020-02-15 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_auto_20200214_2145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenant',
            name='profile_pic',
        ),
    ]
