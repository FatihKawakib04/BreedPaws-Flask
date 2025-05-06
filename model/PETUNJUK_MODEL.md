# Petunjuk Penggunaan Model Machine Learning

## Tentang Model
Aplikasi BreedPaws memerlukan file model machine learning bernama `dog_breed_model.h5` untuk dapat berfungsi dengan baik. Model ini digunakan untuk memprediksi ras anjing dari gambar yang diunggah.

## Cara Mendapatkan Model
1. **Download model** dari sumber yang disediakan oleh pengembang aplikasi
2. **Simpan file model** dengan nama `dog_breed_model.h5` di folder ini (`model/`)
3. **Pastikan nama file tepat** karena aplikasi akan mencari file dengan nama tersebut

## Spesifikasi Model
Model yang digunakan adalah model TensorFlow dengan spesifikasi:
- Input: Gambar RGB dengan ukuran 299x299 piksel
- Output: Probabilitas untuk 10 ras anjing
- Format: H5 (Hierarchical Data Format)

## Ras Anjing yang Didukung
Model ini dapat memprediksi 10 ras anjing berikut:
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

## Troubleshooting
Jika aplikasi menampilkan error saat startup, pastikan:
1. File model `dog_breed_model.h5` ada di folder ini
2. TensorFlow terinstal dengan benar (lihat requirements.txt)
3. Model memiliki format yang benar dan tidak rusak