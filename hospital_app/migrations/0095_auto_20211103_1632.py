# Generated by Django 3.2.8 on 2021-11-03 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0094_auto_20211103_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='building_name',
        ),
        migrations.DeleteModel(
            name='History',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]
