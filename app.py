# app.py
import streamlit as st
from utils.preprocessing import preprocess_image, predict, load_model_keras
from PIL import Image
import time
import os

logo_icon_url = "https://raw.githubusercontent.com/ghiyasakhtar/alzheimer-test/refs/heads/main/logo.png"
warning_icon_url = "https://raw.githubusercontent.com/ghiyasakhtar/alzheimer-test/refs/heads/main/icons8-warning-90.png"
info_icon_url = "https://raw.githubusercontent.com/ghiyasakhtar/alzheimer-test/refs/heads/main/icons8-about-384.png"


# Konfigurasi halaman
st.set_page_config(
    page_title="Deteksi Alzheimer",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Header
st.markdown(f"""
    <div style="text-align: center;">
        <img src="{logo_icon_url}" alt="Logo Aplikasi" style="width: 100px; margin-bottom: 10px;" />
    </div>
    <div style='text-align: center; padding: 10px 30px; background-color: #f9f9f9; border-radius: 12px; margin-bottom: 20px;'>
    <h2 style='font-family: sans-serif; color: #4A90E2;'>
        <span style='font-weight: bold; color: #3B5C87;'>AI</span>zheimer
    </h2>
        <p style='color: #555; font-size: 16px;'>Sistem berbasis deep learning untuk memprediksi tahap perkembangan Alzheimer secara cepat dan otomatis dari citra MRI otak.</p>
    </div>
""", unsafe_allow_html=True)

# Upload gambar MRI
st.markdown("#### Unggah Citra MRI Otak")
uploaded_file = st.file_uploader("Pilih file gambar MRI (format: JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    preprocessed_img, display_img = preprocess_image(uploaded_file)
    with st.spinner("Memprediksi hasil..."):
        model = load_model_keras()

        progress_bar = st.empty()
        for percent_complete in range(0, 101, 5):
            progress_bar.progress(percent_complete)
            time.sleep(0.15)

        # Prediksi dari model
        label, confidence, _ = predict(model, preprocessed_img)

    # Mapping warna background berdasarkan label
    color_map = {
        "Mild Demented": "#e67e22",           # oranye
        "Very Mild Demented": "#f1c40f",      # kuning
        "Non Demented": "#2ecc71",            # hijau
        "Moderate Demented": "#e74c3c"        # merah
    }
    
    bg_color = color_map.get(label, "#95a5a6")  # default abu-abu jika label tidak dikenali

    # Tampilkan hasil prediksi
    st.markdown(f"""
        <div style='padding: 20px; border-radius: 10px; background-color: #f9f9f9; text-align: center; margin-top: 20px; border: 1px solid #ddd;'>
            <div style='display: inline-block; padding: 5px 10px; border-radius: 20px; background-color: {bg_color}; color: white; font-size: 14px;'>
                {label}
            </div>
            <p style='margin-top: 20px; color: #555;'>Confidence: <b>{confidence*100:.2f}%</b></p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='
        padding: 15px;
        border-radius: 10px;
        background-color: #182C44;
        text-align: center;
        color: #C7EBFF;
        font-weight: 600;
        font-size: 16px;
        margin-top: 3px;
    '>
        Prediksi Berhasil
    </div>
    """, unsafe_allow_html=True)

    # Tampilkan gambar yang diupload
    st.markdown("<p style='font-size: 14px; font-weight: 100; text-align: center; color: #f9f9f9; margin-top: 20px; margin-bottom: 5px;'>Citra MRI yang Diupload</p>", unsafe_allow_html=True)
    st.image(display_img, use_container_width=True)
else:
    st.info("Silakan unggah gambar MRI terlebih dahulu untuk memulai prediksi.")

with st.sidebar:
    # Blok informasi
    st.markdown(f"""
    <div style='padding: 15px 20px; background-color: #f9f9f9; border-radius: 12px; margin-top: 10px;'>
        <div style='display: flex; align-items: center; margin-bottom: 10px;'>
            <img src='{info_icon_url}' width='16' style='margin-right: 6px; vertical-align: middle;'/>
            <span style='font-size: 16px; color: #4A90E2; line-height: 1; font-weight: 600;'>Tentang</span>
        </div>
        <p style='color: #333; font-size: 14px; margin-top: 0;'>
            Aplikasi ini menggunakan model Convolutional Neural Network (CNN) untuk mengklasifikasikan kondisi Alzheimer 
            berdasarkan citra MRI otak. Dikembangkan untuk membantu deteksi dini Alzheimer melalui analisis gambar medis.
        </p>
        <p style='color: #555; font-size: 13px;'><strong>Kelas:</strong> Normal, Early Mild Cognitive Impairment, Late Mild Cognitive Impairment, Alzheimer</p>
    </div>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.caption("Created by **CC25-CR428** — 2025")


# Footer & disclaimer
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: #888; font-size: 13px; padding-top: 10px;">
    <img src="{warning_icon_url}" alt="warning" width="20" style="display: block; margin: 0 auto 8px auto;" />
    Hasil ini bukan diagnosis medis dan tidak dimaksudkan sebagai pengganti penilaian medis profesional. <br>
    Konsultasikan dengan ahli medis untuk informasi lebih lanjut. <br><br>
    © 2025 Alzheimer AI | Made with Streamlit
</div>
""", unsafe_allow_html=True)
