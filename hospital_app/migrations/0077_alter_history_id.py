# Generated by Django 3.2.8 on 2021-11-03 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0076_auto_20211103_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='id',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
    ]
