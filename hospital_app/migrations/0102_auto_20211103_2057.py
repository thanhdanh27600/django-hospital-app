# Generated by Django 3.2.8 on 2021-11-03 20:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0101_auto_20211103_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='admitted',
            name='admidssion_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='admitted',
            name='location',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='history',
            name='patient_number',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hospital_app.patient'),
        ),
        migrations.AlterField(
            model_name='history',
            name='room_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hospital_app.room'),
        ),
    ]