# Generated by Django 4.2.7 on 2023-11-25 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('fuel_type', models.CharField(max_length=50)),
                ('mileage_from_odometer', models.FloatField()),
                ('model_date', models.DateField()),
                ('vehicle_engine', models.CharField(max_length=50)),
                ('vehicle_transmission', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
