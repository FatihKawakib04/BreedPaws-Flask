from flask import Flask, render_template, request, jsonify
import json
import os
import random
import logging

# Konfigurasi logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

# Pastikan folder uploads ada
upload_folder = os.path.join('static', 'uploads')
os.makedirs(upload_folder, exist_ok=True)

# Muat label kelas
try:
    with open('model/class_labels.json', 'r') as f:
        class_labels = json.load(f)
    logging.info("Berhasil memuat file class_labels.json")
except Exception as e:
    logging.error(f"Gagal memuat file class_labels.json: {str(e)}")
    class_labels = {str(i): f"Breed-{i}" for i in range(10)}  # Fallback jika file tidak ada

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/contact.html")
def contact():
    return render_template('contact.html')

@app.route("/gallery.html")
def gallery():
    return render_template('gallery.html')

@app.route("/services.html")
def services():
    return render_template('services.html')

@app.route("/predict", methods=['POST'])
def predict():
    if 'image' not in request.files:
        logging.warning("Permintaan prediksi tanpa gambar")
        return jsonify({'error': 'Tidak ada gambar yang diunggah'}), 400
    
    file = request.files['image']
    if file.filename == '':
        logging.warning("Permintaan prediksi dengan nama file kosong")
        return jsonify({'error': 'Tidak ada gambar yang dipilih'}), 400
    
    try:
        # Simpan gambar yang diunggah
        file_path = os.path.join(upload_folder, file.filename)
        file.save(file_path)
        logging.info(f"Gambar berhasil disimpan: {file_path}")
        
        # Mode minimal: selalu menggunakan prediksi dummy
        # Tidak memerlukan TensorFlow atau model ML
        predicted_class = random.randint(0, 9)
        confidence = random.uniform(0.7, 0.99)
        
        breed_name = class_labels[str(predicted_class)]
        if '-' in breed_name:
            breed_name = breed_name.split('-')[1]
        
        # Kembalikan hasil
        result = {
            'success': True,
            'breed': breed_name,
            'confidence': float(confidence),
            'image_path': '/' + file_path.replace('\\', '/'),
            'mode': 'minimal (tanpa model ML)'
        }
        
        logging.info(f"Prediksi berhasil: {breed_name} dengan confidence {confidence:.2f}")
        return jsonify(result)
    except Exception as e:
        logging.error(f"Error saat prediksi: {str(e)}")
        return jsonify({'error': str(e), 'success': False}), 500

@app.route("/team.html")
def team():
    return render_template('team.html')

@app.route("/elements.html")
def elements():
    return render_template('elements.html')

@app.route("/404.html")
def error_page():
    return render_template('404.html')

if __name__ == "__main__":
    print("\n=== MENJALANKAN APLIKASI BREEDPAWS ===")
    print("Mode: Minimal (tanpa TensorFlow)")
    print("Prediksi breed anjing akan menggunakan nilai acak untuk demo")
    print("Server berjalan di http://localhost:5000")
    print("Tekan Ctrl+C untuk menghentikan server\n")
    app.run(debug=True, host='0.0.0.0', port=5000)
