# BreedPaws - Aplikasi Prediksi Ras Anjing

## Tentang Aplikasi

BreedPaws adalah aplikasi web sederhana yang memungkinkan pengguna untuk mengunggah gambar anjing dan mendapatkan prediksi ras anjing tersebut. Aplikasi ini menggunakan Flask sebagai backend dan berjalan dalam mode minimal tanpa memerlukan TensorFlow atau dependensi berat lainnya.

## Cara Menjalankan Aplikasi

### Langkah 1: Instalasi Dependensi

```bash
pip install -r requirements.txt
```

### Langkah 2: Jalankan Aplikasi

```bash
python app.py
```

### Langkah 3: Akses Aplikasi

Buka browser dan kunjungi: http://localhost:5000

## Fitur Utama

- Unggah gambar anjing
- Dapatkan prediksi ras anjing (mode demo dengan nilai acak)
- Tampilan web yang responsif dan menarik
- Tidak memerlukan dependensi berat seperti TensorFlow

## Struktur Folder

- `static/`: Berisi file statis (CSS, JavaScript, gambar)
  - `uploads/`: Folder untuk menyimpan gambar yang diunggah
- `templates/`: Berisi file HTML untuk tampilan web
- `model/`: Berisi file label kelas untuk prediksi

## Troubleshooting

Jika Anda mengalami masalah saat menjalankan aplikasi, silakan lihat `panduan_instalasi_offline.md` untuk solusi dan tips tambahan.

## Prediksi Ras Anjing

Aplikasi ini menggunakan model machine learning TensorFlow untuk memprediksi ras anjing dari gambar yang diunggah.

## Pengembangan Lebih Lanjut

Untuk mengimplementasikan prediksi ras anjing yang sebenarnya, Anda perlu:

1. Menginstal TensorFlow dan dependensi terkait
2. Menyediakan model machine learning yang telah dilatih
3. Memodifikasi kode untuk menggunakan model tersebut

Contoh implementasi dapat dilihat di `model/contoh_penggunaan.txt`.