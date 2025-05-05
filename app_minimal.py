from flask import Flask, render_template, request, jsonify
import json
import os
import random

app = Flask(__name__)

# Muat label kelas
with open('model/class_labels.json', 'r') as f:
    class_labels = json.load(f)

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
        return jsonify({'error': 'Tidak ada gambar yang diunggah'}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'Tidak ada gambar yang dipilih'}), 400
    
    try:
        # Simpan gambar yang diunggah
        upload_folder = os.path.join('static', 'uploads')
        os.makedirs(upload_folder, exist_ok=True)
        file_path = os.path.join(upload_folder, file.filename)
        file.save(file_path)
        
        # Mode minimal: selalu menggunakan prediksi dummy
        # Tidak memerlukan TensorFlow atau model ML
        predicted_class = random.randint(0, 9)
        confidence = random.uniform(0.7, 0.99)
        
        # Kembalikan hasil
        result = {
            'success': True,
            'breed': class_labels[str(predicted_class)].split('-')[1],
            'confidence': float(confidence),
            'image_path': '/' + file_path.replace('\\', '/'),
            'mode': 'minimal (tanpa model ML)'
        }
        
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/team.html")
def team():
    return render_template('team.html')

@app.route("/404.html")
def error_page():
    return render_template('404.html')

if __name__ == "__main__":
    print("\n=== MENJALANKAN APLIKASI DALAM MODE MINIMAL ===")
    print("Mode ini tidak memerlukan TensorFlow atau dependensi berat lainnya")
    print("Prediksi breed anjing akan menggunakan nilai acak untuk demo")
    print("Untuk menggunakan model ML asli, instal semua dependensi dan gunakan app.py\n")
    app.run(debug=True)