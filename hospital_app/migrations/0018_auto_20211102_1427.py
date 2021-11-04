# Generated by Django 3.2.8 on 2021-11-02 07:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0017_car'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admitted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('building_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('number_of_floors', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='HeadOfCamp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('history_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('transfer_date', models.DateField(default=django.utils.timezone.now)),
                ('destination_room', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='MedicationEffect',
            fields=[
                ('effect_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_app.medication')),
            ],
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Invalid phone number (Vietnamese only)', regex='/^(0?)(3[2-9]|5[6|8|9]|7[0|6-9]|8[0-6|8|9]|9[0-4|6-9])[0-9]{7}$/')])),
                ('gender', models.BooleanField(choices=[('M', 'Male'), ('F', 'Female')])),
                ('address', models.TextField()),
                ('identify_number', models.IntegerField()),
                ('nurse_id', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PatientComobidity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_app.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('personal_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Invalid phone number (Vietnamese only)', regex='/^(0?)(3[2-9]|5[6|8|9]|7[0|6-9]|8[0-6|8|9]|9[0-4|6-9])[0-9]{7}$/')])),
                ('gender', models.BooleanField(choices=[('M', 'Male'), ('F', 'Female')])),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('date_of_birth', models.DateField(default=django.utils.timezone.now)),
                ('type', models.CharField(choices=[('N', 'Nurse'), ('S', 'Staff'), ('D', 'Doctor'), ('H', 'Head of camp')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ReceiveTreatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(default=django.utils.timezone.now)),
                ('result', models.TextField()),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_app.medication')),
                ('number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_app.patient')),
                ('personal_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_app.personnel')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('floor', models.IntegerField()),
                ('maximum_capacity', models.IntegerField()),
                ('room_type', models.CharField(choices=[('Normal', 'Normal room'), ('Emergency', 'Emergency room'), ('Recuper.', 'Recuperation room')], max_length=50)),
                ('building_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_app.building')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_app.personnel')),
            ],
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('symptom_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(default=django.utils.timezone.now)),
                ('symptom_name', models.CharField(max_length=50)),
                ('number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_app.patient')),
            ],
        ),
        migrations.CreateModel(
            name='TestInfomation',
            fields=[
                ('test_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=10)),
                ('test_date', models.DateField(default=django.utils.timezone.now)),
                ('positivity', models.BooleanField()),
                ('type', models.CharField(choices=[('PCR', 'PCR test'), ('Quick', 'Quick test'), ('SPO2', 'SPO2 test'), ('Resp.', 'Respiratory rate')], max_length=50)),
                ('condition', models.TextField()),
                ('number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_app.patient')),
            ],
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.AddField(
            model_name='nurse',
            name='nurse_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_app.personnel'),
        ),
        migrations.AddField(
            model_name='history',
            name='number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_app.patient'),
        ),
        migrations.AddField(
            model_name='history',
            name='room_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_app.room'),
        ),
        migrations.AddField(
            model_name='headofcamp',
            name='head_of_camp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_app.personnel'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='doctor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_app.personnel'),
        ),
        migrations.AddField(
            model_name='admitted',
            name='number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_app.patient'),
        ),
        migrations.AddField(
            model_name='admitted',
            name='personnel_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_app.personnel'),
        ),
        migrations.AddField(
            model_name='admitted',
            name='test_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital_app.testinfomation'),
        ),
    ]
