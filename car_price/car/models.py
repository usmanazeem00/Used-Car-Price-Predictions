from django.db import models

class Vehicle(models.Model):
    brand = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=50)
    mileage_from_odometer = models.FloatField()
    model_date = models.DateField()
    vehicle_engine = models.CharField(max_length=50)
    vehicle_transmission = models.CharField(max_length=50)
    price = models.IntegerField()
