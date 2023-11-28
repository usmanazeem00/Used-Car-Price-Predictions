from django.urls import path
from .views import home, get_descriptions, get_fuels

urlpatterns = [
    path('', home, name='home'),
    path('get_descriptions', get_descriptions, name='get_descriptions'),
    path('get_fuels', get_fuels, name='get_fuels')
]