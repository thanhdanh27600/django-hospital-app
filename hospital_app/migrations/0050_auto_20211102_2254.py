# Generated by Django 3.2.8 on 2021-11-02 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0049_auto_20211102_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testinfomation',
            name='id',
        ),
        migrations.AddField(
            model_name='testinfomation',
            name='test_id',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
    ]