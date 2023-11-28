import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import joblib 
df=pd.read_csv('TrainingData.csv')

def train_random_forest(df, save_path='trained_model'):
    # Select features
    X = df.drop(columns=['price'])
    y = df['price']
    # Categorical encoding for 'brand', 'description', and 'vehicle_transmission'
    le_brand = LabelEncoder()
    le_description = LabelEncoder()
    le_transmission = LabelEncoder()
    X['brand'] = le_brand.fit_transform(X['brand'])
    X['description'] = le_description.fit_transform(X['description'])
    X['vehicle_transmission'] = le_transmission.fit_transform(X['vehicle_transmission'])
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Create a MinMaxScaler instance
    scaler = MinMaxScaler()
    # Fit the scaler to the training data and transform both the training and test data
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    # Create a Random Forest Regressor model
    rf_model = RandomForestRegressor(random_state=42)
    # Train the Random Forest model on the scaled data
    rf_model.fit(X_train_scaled, y_train)
    # Make predictions on the scaled test set
    y_pred_rf = rf_model.predict(X_test_scaled)
    r2_rf = r2_score(y_test, y_pred_rf)
    accuracy_percentage_rf = r2_rf * 100
    print(f"Random Forest Accuracy: {accuracy_percentage_rf:.2f}%")
    #Saving Important Things
    joblib.dump(rf_model, f'{save_path}_model.joblib')
    joblib.dump(scaler, f'{save_path}_scaler.joblib')
    joblib.dump(le_brand, f'{save_path}_label_encoder_brand.joblib')
    joblib.dump(le_description, f'{save_path}_label_encoder_description.joblib')
    joblib.dump(le_transmission, f'{save_path}_label_encoder_transmission.joblib')
    print(f"Trained model, scaler, and label encoders saved to {save_path}")

train_random_forest(df)