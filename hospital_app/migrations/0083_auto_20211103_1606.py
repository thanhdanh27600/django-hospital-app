# Generated by Django 3.2.8 on 2021-11-03 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0082_rename_number_testinfomation_patient_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='building_name',
        ),
        migrations.AddField(
            model_name='building',
            name='id',
            field=models.BigAutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]