# Generated by Django 3.2.8 on 2021-11-03 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0062_auto_20211103_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientcomobidity',
            name='comobidity_name',
        ),
    ]