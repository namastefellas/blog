# Generated by Django 3.2.3 on 2021-05-23 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20210517_1146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='likes',
        ),
    ]
