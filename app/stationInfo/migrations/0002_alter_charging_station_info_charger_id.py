# Generated by Django 5.0.3 on 2024-03-13 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stationInfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charging_station_info',
            name='Charger_ID',
            field=models.TextField(default=''),
        ),
    ]