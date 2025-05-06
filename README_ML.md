# BreedPaws - Aplikasi Prediksi Ras Anjing dengan Machine Learning

## Tentang Aplikasi
BreedPaws adalah aplikasi web yang menggunakan model machine learning untuk memprediksi ras anjing dari gambar yang diunggah. Aplikasi ini dibangun dengan Flask dan menggunakan model TensorFlow yang telah dilatih untuk mengenali 10 ras anjing populer.

## Fitur Utama
- Prediksi ras anjing menggunakan model machine learning
- Antarmuka web yang mudah digunakan
- Menampilkan hasil prediksi dengan tingkat keyakinan (confidence)

## Cara Penggunaan

### Persyaratan
Pastikan Anda telah menginstal semua dependensi yang diperlukan:
```
pip install -r requirements.txt
```

### Menjalankan Aplikasi
```
python app.py
```

Aplikasi akan berjalan di http://localhost:5000

### Cara Menggunakan
1. Buka browser dan akses http://localhost:5000
2. Pilih gambar anjing yang ingin diprediksi
3. Klik tombol "Prediksi"
4. Hasil prediksi akan ditampilkan beserta tingkat keyakinan

## Struktur Model
Model machine learning yang digunakan adalah model dalam format H5 yang terletak di folder `model/dog-breed_model.h5`. Model ini dapat memprediksi 10 ras anjing berikut:

1. Chihuahua
2. Maltese Dog
3. Shih-Tzu
4. Golden Retriever
5. Labrador Retriever
6. Rottweiler
7. German Shepherd
8. French Bulldog
9. Siberian Husky
10. Pomeranian

## Mode Aplikasi
Aplikasi ini menggunakan model machine learning untuk prediksi ras anjing:

- Menggunakan model TensorFlow untuk prediksi yang akurat
- Memerlukan file model dog_breed_model.h5 di folder model/

## Pemecahan Masalah

- **TensorFlow Error**: Pastikan Anda menginstal versi TensorFlow yang kompatibel dengan sistem operasi Anda
- **Model tidak dimuat**: Periksa apakah file model `dog-breed_model.h5` ada di folder `model/`
- **Gambar tidak dapat diproses**: Pastikan gambar dalam format yang didukung (JPG, PNG)

## Pengembangan Lebih Lanjut

Untuk pengembangan lebih lanjut, Anda dapat:
1. Menambahkan lebih banyak ras anjing ke model
2. Meningkatkan akurasi model dengan data pelatihan tambahan
3. Menambahkan fitur seperti riwayat prediksi atau perbandingan ras