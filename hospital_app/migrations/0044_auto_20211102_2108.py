# Generated by Django 3.2.8 on 2021-11-02 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0043_auto_20211102_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='headofcamp',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='headofcamp',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='nurse',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='nurse',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='symptom',
            name='symptom_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]