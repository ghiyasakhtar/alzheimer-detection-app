# **AI**zheimer
**AI**zheimer adalah aplikasi berbasis AI yang dikembangkan untuk membantu deteksi dini penyakit Alzheimer melalui analisis citra MRI otak. Proyek ini menggabungkan kekuatan *Convolutional Neural Network (CNN)*, antarmuka interaktif menggunakan **Streamlit**, dan sistem rekomendasi berbasis visual untuk meningkatkan akurasi dan kenyamanan diagnosis awal.

## Tujuan Proyek
Memberdayakan sistem kesehatan dengan solusi **AI yang cepat, inklusif, dan dapat diakses** oleh siapa saja, dalam rangka meningkatkan deteksi dini Alzheimer dan membantu proses diagnosis klinis.

## Fitur Utama

-  Web interaktif berbasis Streamlit
- Model klasifikasi CNN untuk mendeteksi:
  - Normal
  - Very Mild Demented
  - Mild Demented
  - Moderate Demented
- Visualisasi hasil prediksi dan probabilitas
- Upload gambar MRI otak dengan preprocessing otomatis
- Sistem rekomendasi gambar sejenis berdasarkan kemiripan fitur


## Teknologi yang Digunakan
- Python 3.10
- TensorFlow / Keras
- OpenCV & Pillow
- Scikit-learn
- Streamlit
- NumPy, Pandas, Matplotlib


## Cara Menjalankan Proyek

### 1. Clone Repository
```bash
git clone https://github.com/ghiyasakhtar/alzheimer-detection-app
cd alzheimer-detection-app
```

### 2. Install 
Gunakan pip:
```bash
pip install -r requirements.txt
```

### 3. Jalankan Aplikasi
```bash
streamlit run app.py
```

## Struktur Proyek

```
alzheimer-detection-app/
├── app.py                      # File utama untuk menjalankan aplikasi Streamlit
├── utils/
│ └── preprocessing.py          # Modul untuk preprocessing gambar MRI
├── assets/                     # Folder berisi aset visual untuk tampilan aplikasi
│ ├── logo.png                  # Logo aplikasi
│ ├── warning.png               # Icon peringatan
│ ├── about.png                 # Gambar/about untuk halaman informasi
│ └── screenshot.jpg            # Screenshot antarmuka aplikasi
├── AlzheimerCapstone.h5        # Model CNN terlatih untuk deteksi Alzheimer
├── Alzheimer_CapstoneV5.ipynb  # Notebook eksplorasi & pengembangan model
├── requirements.txt            # Daftar dependensi Python yang dibutuhkan
├── README.md                   # Dokumentasi proyek (file ini)
└── .gitattributes              # File konfigurasi Git untuk penanganan atribut file
```

## Tampilan Aplikasi
<img src="https://raw.githubusercontent.com/ghiyasakhtar/alzheimer-detection-app/refs/heads/main/assets/screenshot.jpg" alt="Preview Aplikasi" width="600"/>

---

### Other Resources
* **Deployed Site:** [aizheimer.streamlit.app/](https://aizheimer.streamlit.app/)
* **Dataset:** [Augmented Alzheimer MRI Dataset | Kaggle](https://www.kaggle.com/datasets/uraninjo/augmented-alzheimer-mri-dataset)
* **Video Presentation:** [YouTube Link (Unlisted)](https://youtu.be/fiFNzQ26de4)
* **Presentation Slides:** [Presentation - AI for Alzheimer’s Detection | Canva](https://www.canva.com/design/DAGqOReI5BU/QHycU29GQMjtF-OenbprfA/edit?utm_content=DAGqOReI5BU&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
