# Generated by Django 3.2.8 on 2021-11-02 14:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0044_auto_20211102_2108'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receivetreatment',
            old_name='personal_id',
            new_name='doctor_id',
        ),
        migrations.RenameField(
            model_name='receivetreatment',
            old_name='code',
            new_name='medication_code',
        ),
        migrations.AddField(
            model_name='medication',
            name='expiration_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='medication',
            name='name',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='medication',
            name='price',
            field=models.FloatField(default=None),
        ),
    ]