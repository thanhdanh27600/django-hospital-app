# Generated by Django 3.2.8 on 2021-11-03 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0084_auto_20211103_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='building_name',
        ),
        migrations.RemoveField(
            model_name='building',
            name='number_of_floors',
        ),
        migrations.AlterField(
            model_name='building',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]