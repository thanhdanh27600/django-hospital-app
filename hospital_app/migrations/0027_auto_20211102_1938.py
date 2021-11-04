# Generated by Django 3.2.8 on 2021-11-02 12:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0026_auto_20211102_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.BigIntegerField(default=None, primary_key=True, serialize=False)),
                ('address', models.TextField(default=None)),
                ('phone', models.CharField(default=None, max_length=12, validators=[django.core.validators.RegexValidator(message='Invalid phone number (Vietnamese only)', regex='^(0?)(3[2-9]|5[6|8|9]|7[0|6-9]|8[0-6|8|9]|9[0-4|6-9])[0-9]{7}$')])),
                ('gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('NOT PROVIDED', 'Not Provided')], default='NOT PROVIDED', max_length=12)),
                ('first_name', models.CharField(default=None, max_length=25)),
                ('last_name', models.CharField(default=None, max_length=25)),
                ('date_of_birth', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.CharField(choices=[('NURSE', 'Nurse'), ('STAFF', 'Staff'), ('DOCTOR', 'Doctor'), ('HEAD', 'Head of camp')], default='STAFF', max_length=50)),
                ('personnel_id', models.CharField(default=None, editable=False, max_length=50, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='patient',
            name='number',
            field=models.BigIntegerField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='nurse_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hospital_app.nurse'),
        ),
    ]
