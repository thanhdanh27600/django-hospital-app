# Generated by Django 3.2.8 on 2021-11-02 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0052_admitted_testinfomation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testinfomation',
            name='number',
        ),
        migrations.DeleteModel(
            name='Admitted',
        ),
        migrations.DeleteModel(
            name='TestInfomation',
        ),
    ]