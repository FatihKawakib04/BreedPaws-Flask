from flask import Flask, render_template, request, jsonify
import json
import os
import logging
import numpy as np
from PIL import Image
import tensorflow as tf

# Konfigurasi logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

# Pastikan folder uploads ada
upload_folder = os.path.join('static', 'uploads')
os.makedirs(upload_folder, exist_ok=True)

# Muat model dan label kelas
try:
    # Muat model
    model_path = 'model/dog_breed_model.h5'
    model = tf.keras.models.load_model(model_path)
    logging.info(f"Berhasil memuat model dari {model_path}")
    
    # Muat label kelas
    with open('model/class_labels.json', 'r') as f:
        class_labels = json.load(f)
    logging.info("Berhasil memuat file class_labels.json")
    
    # Tentukan ukuran input model
    input_shape = model.input_shape[1:3]  # Ambil dimensi tinggi dan lebar
    logging.info(f"Ukuran input model: {input_shape}")
    
except Exception as e:
    logging.error(f"Gagal memuat model atau label: {str(e)}")
    error_message = f"Model ML tidak dapat dimuat: {str(e)}. Pastikan:\n"
    error_message += "1. File model/dog_breed_model.h5 tersedia dan tidak rusak\n"
    error_message += "2. File model/class_labels.json tersedia dan valid\n"
    error_message += "3. TensorFlow terinstal dengan benar (lihat requirements.txt)"
    raise Exception(error_message)

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

def preprocess_image(image_path, target_size):
    """Praproses gambar untuk input model"""
    try:
        img = Image.open(image_path)
        img = img.resize(target_size)  # Resize sesuai input model
        img = img.convert('RGB')  # Pastikan gambar RGB
        
        # Normalisasi gambar
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)  # Tambahkan dimensi batch
        
        return img_array
    except Exception as e:
        logging.error(f"Error saat preprocessing gambar: {str(e)}")
        raise

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
        
        # Praproses gambar
        img_array = preprocess_image(file_path, input_shape)
        
        # Prediksi
        predictions = model.predict(img_array)
        predicted_class = np.argmax(predictions, axis=1)[0]
        confidence = float(predictions[0][predicted_class])
        
        # Dapatkan nama breed
        breed_name = class_labels[str(predicted_class)]
        if '-' in breed_name:
            breed_name = breed_name.split('-')[1]
            
        logging.info(f"Prediksi berhasil: {breed_name} dengan confidence {confidence:.2f}")
        
        # Kembalikan hasil
        result = {
            'success': True,
            'breed': breed_name,
            'confidence': float(confidence),
            'image_path': '/' + file_path.replace('\\', '/')
        }
        
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
    print(f"Model ML berhasil dimuat: {model_path}")
    print(f"Ukuran input model: {input_shape}")
    print("Aplikasi berjalan dengan model Machine Learning")
    print("Server berjalan di http://localhost:5000")
    print("Tekan Ctrl+C untuk menghentikan server\n")
    app.run(debug=True, host='0.0.0.0', port=5000)
