# Generated by Django 3.2.8 on 2021-11-03 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0081_auto_20211103_1516'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testinfomation',
            old_name='number',
            new_name='patient_number',
        ),
    ]
