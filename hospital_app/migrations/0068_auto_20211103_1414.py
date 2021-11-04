# Generated by Django 3.2.8 on 2021-11-03 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0067_auto_20211103_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientcomobidity',
            name='id',
        ),
        migrations.AddField(
            model_name='patientcomobidity',
            name='comobidity_name',
            field=models.CharField(default=None, max_length=50, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AddField(
            model_name='patientcomobidity',
            name='patient_number',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hospital_app.patient'),
            preserve_default=False,
        ),
    ]