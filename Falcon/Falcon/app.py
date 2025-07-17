from flask import Flask, request, jsonify, send_from_directory
import io
import base64
from PIL import Image
from ultralytics import YOLO
import os
from flask_cors import CORS

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)  # Enable CORS for all routes

# Load YOLOv8 model (ensure best.pt is in the same directory)
model = YOLO('best.pt')

@app.route('/')
def root():
    return send_from_directory('.', 'index.html')

@app.route('/detect', methods=['POST'])
def detect():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    file = request.files['image']
    img = Image.open(file.stream).convert('RGB')
    # Run detection
    results = model(img)
    # Plot results on image
    annotated_img = results[0].plot()
    # Convert to PNG and base64
    img_bytes = io.BytesIO()
    Image.fromarray(annotated_img).save(img_bytes, format='PNG')
    img_bytes.seek(0)
    base64_img = base64.b64encode(img_bytes.read()).decode('utf-8')
    return jsonify({'detected_image_url': f'data:image/png;base64,{base64_img}'})

# Serve any other static files (css, js, etc.)
@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run(debug=True) 