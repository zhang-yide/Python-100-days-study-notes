# Generated by Django 2.2.7 on 2019-11-21 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191121_1359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='bad_count',
        ),
        migrations.RemoveField(
            model_name='post',
            name='good_count',
        ),
    ]
