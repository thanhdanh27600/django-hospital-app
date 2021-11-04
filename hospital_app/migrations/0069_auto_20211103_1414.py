# Generated by Django 3.2.8 on 2021-11-03 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0068_auto_20211103_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientcomobidity',
            name='id',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='patientcomobidity',
            name='comobidity_name',
            field=models.CharField(default=None, max_length=50, unique=True),
        ),
    ]
