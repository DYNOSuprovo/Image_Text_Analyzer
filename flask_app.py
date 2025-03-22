### Flask App (Model 1 - Image-to-Text Extraction)
from flask import Flask, request, jsonify
from PIL import Image
import pytesseract
import io

app = Flask(__name__)

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

@app.route('/extract-text', methods=['POST'])
def extract_text():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    
    image = request.files['image']
    img = Image.open(io.BytesIO(image.read()))
    extracted_text = pytesseract.image_to_string(img)
    
    return jsonify({'extracted_text': extracted_text})

if __name__ == '__main__':
    app.run(debug=True, port=5000)