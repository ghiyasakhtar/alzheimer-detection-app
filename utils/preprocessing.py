from PIL import Image
import numpy as np
import streamlit as st
# import joblib
from tensorflow.keras.models import load_model
# import gdown
# import os

# File ID dari Google Drive
# file_id = '1gmBSOP3BIAnCvAnuPBQs1TlVuMIQ31ld'
# output_path = 'AlzheimerCapstone.h5'
# gdrive_url = f'https://drive.google.com/uc?id={file_id}'

# Load model Keras dari file .h5
@st.cache_resource
def load_model_keras():
    # model = joblib.load("AlzheimerCapstone.pkl")
    model = load_model("AlzheimerCapstone.h5")
    return model

# Preprocessing gambar
def preprocess_image(image_file):
    image = Image.open(image_file).convert("RGB")
    image = image.resize((256, 256))
    image_array = np.array(image) / 255.0  # Normalisasi [0, 1]
    image_array = np.expand_dims(image_array, axis=0)  # Jadi (1, 256, 256, 3)
    return image_array, image

# Prediksi dari model
def predict(model, preprocessed_image):
    class_names = [
        "Mild Demented",
        "Moderate Demented",
        "Non Demented",
        "Very Mild Demented"
    ]
    probabilities = model.predict(preprocessed_image)[0]  # Ambil baris pertama
    predicted_index = np.argmax(probabilities)
    label = class_names[predicted_index]
    confidence = probabilities[predicted_index]
    return label, confidence, dict(zip(class_names, probabilities))
