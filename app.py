import streamlit as st
import pandas as pd
import joblib

# Load model & feature columns
model = joblib.load('house_model.pkl')
feature_columns = joblib.load('feature_columns.pkl')

st.title("🏠 House Price Predictor")
st.write("Isi data rumah di bawah ini untuk memprediksi harganya.")

# Form input sesuai fitur training
bedrooms = st.number_input("Jumlah Kamar Tidur", 1, 10, 3)
bathrooms = st.number_input("Jumlah Kamar Mandi", 1, 10, 2)
first_flr_sf = st.number_input("Luas Lantai 1 (sqft)", 500, 3000, 1500)
living_area = st.number_input("Luas Bangunan (Gr Liv Area)", 500, 5000, 1800)
overall_qual = st.slider("Kualitas Bangunan (1-10)", 1, 10, 5)

# Buat dataframe sesuai urutan feature_columns
data = pd.DataFrame({
    'Bedroom AbvGr': [bedrooms],
    'Full Bath': [bathrooms],
    '1st Flr SF': [first_flr_sf],
    'Gr Liv Area': [living_area],
    'Overall Qual': [overall_qual]
})

# Pastikan urutannya sama persis
data = data[feature_columns]

# Predict button
if st.button("Prediksi Harga"):
    price = model.predict(data)[0]
    st.success(f"💰 Estimasi Harga Rumah: ${price:,.2f}")