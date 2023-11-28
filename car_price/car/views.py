from django.shortcuts import render
from django.http import JsonResponse
import joblib
import pandas as pd
import json

fuels = ['Diesel', 'Electric', 'Hybrid', 'Lpg', 'Petrol']
brands = {}
with open('brands.json', 'r') as json_file:
    brands = json.load(json_file)
print(brands)

brands_fuels = {}
with open('brand_fuels.json', 'r') as json_file:
    brands_fuels = json.load(json_file)
print(brands_fuels)


def load_model(save_path='trained_model'):
    # Loading saved model,scalres from the disk
    rf_model = joblib.load(f'{save_path}_model.joblib')
    scaler = joblib.load(f'{save_path}_scaler.joblib')
    le_brand = joblib.load(f'{save_path}_label_encoder_brand.joblib')
    le_description = joblib.load(f'{save_path}_label_encoder_description.joblib')
    le_transmission = joblib.load(f'{save_path}_label_encoder_transmission.joblib')
    return rf_model, scaler, le_brand, le_description, le_transmission

trained_model, trained_scaler, label_encoder_brand, label_encoder_description, label_encoder_transmission = load_model()



def predict_price(user_input, model, scaler, le_brand, le_description, le_transmission): 
    # Convert the user input into a DataFrame
    user_df = pd.DataFrame([user_input])
 
    # Categorical encoding for 'brand', 'description', and 'vehicle_transmission' using the trained LabelEncoders
    user_df['brand'] = le_brand.transform(user_df['brand'])
    user_df['description'] = le_description.transform(user_df['description'])  
    user_df['vehicle_transmission'] = le_transmission.transform(user_df['vehicle_transmission'])

    # Scale the user input data using the same scaler used for training
    user_scaled = scaler.transform(user_df)

    # Make predictions using the trained Random Forest model
    user_price_prediction = model.predict(user_scaled)

    return user_price_prediction[0]



def home(request): 
    response = {'brands': brands.keys()}

    if request.method == 'POST':
        user_data = {}
        user_data['brand'] = request.POST.get('brand')
        user_data['description'] = request.POST.get('description')
        user_data['mileage_from_odometer'] = int(request.POST.get('mileage_from_odometer'))
        user_data['model_date'] = int(request.POST.get('model_date'))
        user_data['vehicle_engine'] = int(request.POST.get('vehicle_engine'))
        user_data['vehicle_transmission'] = request.POST.get('vehicle_transmission')
        response['fuel_type'] = request.POST.get('fuel_type')
        for fuel in fuels:
            user_data[f'fuel_{fuel}'] = int(response['fuel_type'] == fuel)

        user_data['price'] = predict_price(user_data, trained_model, trained_scaler, label_encoder_brand, label_encoder_description, label_encoder_transmission)
        response.update(user_data)

    return render(request, 'home.html', response)
 
def get_descriptions(request):
    brand = request.GET.get('brand')
    print(brand)
    return JsonResponse({'description_choices': brands[brand]})

def get_fuels(request):
    description = request.GET.get('description')
    return JsonResponse({'fuel_choices': brands_fuels[description]})