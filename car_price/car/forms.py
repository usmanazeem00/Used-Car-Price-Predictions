# myapp/forms.py
from django import forms
from .models import Vehicle

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['brand', 'fuel_type', 'mileage_from_odometer', 'model_date', 'vehicle_engine', 'vehicle_transmission']
