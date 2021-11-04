# Generated by Django 3.2.8 on 2021-11-03 16:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0095_auto_20211103_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('room_id', models.CharField(default=None, editable=False, max_length=50, null=True)),
                ('floor', models.IntegerField()),
                ('maximum_capacity', models.IntegerField()),
                ('room_type', models.CharField(choices=[('NORMAL', 'Normal room'), ('EMERGENCY', 'Emergency room'), ('RECUP.', 'Recuperation room')], max_length=50)),
                ('building_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_app.building')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('transfer_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('destination_room', models.CharField(max_length=50)),
                ('patient_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_app.patient')),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_app.room')),
            ],
        ),
    ]