from django.shortcuts import render

fuels = ['Petrol', 'Hybrid', 'Diesel', 'CNG', 'Electric', 'Lpg']
brands = ['MG', 'Toyota', 'Honda', 'KIA', 'Nissan', 'Suzuki', 'Mercedes Benz'
            'Range Rover', 'Daihatsu', 'Changan', 'BMW', 'Hyundai', 'Mazda', 'Haval', 'DFSK'
            'Mitsubishi', 'Audi', 'Chevrolet', 'Porsche', 'United', 'Others', 'FAW', 'Lexus'
            'Prince', 'Chrysler', 'Subaru', 'Peugeot', 'Ford', 'Land Rover', 'Master'
            'Volkswagen', 'Chery', 'Willys', 'Proton', 'Jeep', 'MINI', 'SsangYong', 'Isuzu'
            'Daewoo', 'Daehan', 'BAIC', 'Tesla', 'Cadillac', 'Datsun', 'Adam', 'Hummer'
            'Alfa Romeo', 'Sogo', 'Golf', 'Jaguar', 'Dodge', 'Hino', 'Buick', 'Morris'
            'JW Forland', 'Bentley', 'JAC', 'Fiat', 'Roma', 'JMC', 'Ferrari', 'Geely'
            'ZOTYE', 'Opel', 'Vauxhall', 'Oldsmobile', 'GMC', 'Citroen', 'Classic Cars'
            'Mushtaq', 'Volvo']

def home(request): 
    response = {'fuel_types': fuels, 'brands': brands}

    if request.method == 'POST':
        print("Form submitted")
        response['brand'] = request.POST.get('brand')
        response['fuel_type'] = request.POST.get('fuel_type')
        response['mileage_from_odometer'] = request.POST.get('mileage_from_odometer')
        response['model_date'] = request.POST.get('model_date')
        response['vehicle_engine'] = request.POST.get('vehicle_engine')
        response['vehicle_transmission'] = request.POST.get('vehicle_transmission')
        response['price'] = int(response['model_date']) * int(response['vehicle_engine']) * int(response['mileage_from_odometer'])

    return render(request, 'home.html', response)
