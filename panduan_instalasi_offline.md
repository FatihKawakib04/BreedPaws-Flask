# Panduan Instalasi dan Penggunaan BreedPaws

## Cara Cepat Menjalankan Aplikasi

1. Instal dependensi minimal:
   ```
   pip install -r requirements.txt
   ```

2. Jalankan aplikasi:
   ```
   python app.py
   ```

3. Buka browser dan akses: http://localhost:5000

## Solusi untuk Masalah Koneksi Internet

Jika Anda mengalami masalah koneksi internet saat menginstal paket, berikut adalah beberapa solusi:

### 1. Instalasi Offline dengan Paket yang Sudah Diunduh

```
pip install --no-index --find-links=./packages -r requirements.txt
```

### 2. Mengunduh Paket Secara Manual (dari komputer lain)

```
# Di komputer dengan koneksi internet
pip download -r requirements.txt -d ./packages

# Salin folder 'packages' ke komputer tanpa koneksi internet
# Kemudian di komputer tanpa koneksi internet
pip install --no-index --find-links=./packages -r requirements.txt
```

### 3. Instalasi Minimal (hanya Flask)

Jika Anda hanya ingin menjalankan aplikasi web dasar:

```
pip install flask==2.0.1
```

## Struktur Folder Penting

- `static/uploads/`: Folder untuk menyimpan gambar yang diunggah (dibuat otomatis)
- `model/`: Berisi file label kelas untuk prediksi
- `templates/`: Berisi file HTML untuk tampilan web

## Informasi Versi

Aplikasi ini menggunakan:
- Flask 2.0.1
- Werkzeug 2.0.1
- Jinja2 3.0.1
- Pillow 8.3.1

## Catatan Penting

Aplikasi ini memerlukan TensorFlow dan model machine learning untuk berfungsi dengan baik. Pastikan file model dog_breed_model.h5 tersedia di folder model/.

## Troubleshooting

- **Error saat menjalankan aplikasi**: Pastikan semua dependensi terinstal dengan benar
- **Gambar tidak muncul**: Periksa folder `static/uploads/` sudah ada dan memiliki izin yang benar
- **Prediksi tidak berfungsi**: Periksa file `model/class_labels.json` ada dan berformat benar
- NumPy 1.21.2
- TensorFlow 2.6.0

Untuk pengembangan, Anda dapat menjalankan aplikasi tanpa TensorFlow jika hanya ingin menguji antarmuka web tanpa fitur prediksi.