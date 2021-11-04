# Generated by Django 3.2.8 on 2021-11-03 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0080_auto_20211103_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicationeffect',
            name='code',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hospital_app.medication'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='receivetreatment',
            name='medication_code',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hospital_app.medication'),
            preserve_default=False,
        ),
    ]
