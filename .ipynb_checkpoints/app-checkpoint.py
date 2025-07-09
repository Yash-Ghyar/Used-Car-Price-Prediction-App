import streamlit as st
import pickle

# Define mappings
brand_map = {
    'Honda': 1, 'Toyota': 2, 'Volkswagen': 3, 'Maruti Suzuki': 4, 'BMW': 5, 'Ford': 6,
    'Kia': 7, 'Mercedes-Benz': 8, 'Hyundai': 9, 'Audi': 10, 'Renault': 11, 'MG': 11,
    'Volvo': 12, 'Skoda': 13, 'Tata': 14, 'Mahindra': 15, 'Mini': 16, 'Land Rover': 17,
    'Jeep': 18, 'Chevrolet': 18, 'Jaguar': 19, 'Fiat': 20, 'Aston Martin': 21, 'Porsche': 22,
    'Nissan': 23, 'Force': 24, 'Mitsubishi': 25, 'Lexus': 26, 'Isuzu': 27, 'Datsun': 28,
    'Ambassador': 29, 'Rolls-Royce': 30, 'ICML': 31, 'Bajaj': 32, 'Opel': 33, 'Ashok': 34,
    'Bentley': 35, 'Ssangyong': 36, 'Maserati': 37
}

transmission_map = {'Manual': 0, 'Automatic': 1}
fuel_map = {'Petrol': 0, 'Diesel': 1, 'CNG': 2, 'Hybrid': 3}

# Load model
try:
    model = pickle.load(open('modelcar.pkl', 'rb'))
except Exception as e:
    st.error(f"❌ Failed to load model: {e}")
    st.stop()

# UI
st.title("🚗 Used Car Price Prediction")
st.write("Enter the car details below:")

# Brand dropdown
brand_input = st.selectbox("Brand", sorted(brand_map.keys()))

# Manufacturing year as dropdown
year = st.selectbox("Manufacturing Year", list(reversed(range(1990, 2025))))

# Kilometers driven as dropdown
km_options = {
    "0 - 10,000": 5000,
    "10,001 - 30,000": 20000,
    "30,001 - 50,000": 40000,
    "50,001 - 70,000": 60000,
    "70,001 - 100,000": 85000,
    "100,001 - 150,000": 125000,
    "150,001+": 160000
}
km_label = st.selectbox("Kilometers Driven", list(km_options.keys()))
km_driven = km_options[km_label]

# Other dropdowns
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.selectbox("Owner", ["First", "Second", "Third", "Fourth+"])
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "Hybrid"])

# Predict button
if st.button("Predict Price"):
    try:
        brand_enc = brand_map[brand_input]
        transmission_enc = transmission_map[transmission]
        fuel_enc = fuel_map[fuel_type]
        owner_enc = ["First", "Second", "Third", "Fourth+"].index(owner) + 1
        age = 2024 - year

        input_data = [[brand_enc, age, km_driven, transmission_enc, owner_enc, fuel_enc]]

        prediction = model.predict(input_data)[0]
        st.success(f"💰 Predicted Price: ₹{prediction:,.2f}")
    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")



