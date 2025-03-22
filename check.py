from flask import Flask, render_template, request
from PIL import Image
import pytesseract
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

@app.route('/', methods=['GET', 'POST'])
def index():
    ocr_text = None
    image_url = None
    
    if request.method == 'POST':
        if 'image' in request.files:
            img_file = request.files['image']
            if img_file.filename != '':
                img_path = os.path.join(UPLOAD_FOLDER, img_file.filename)
                img_file.save(img_path)
                
                # Process image
                img = Image.open(img_path)
                ocr_text = pytesseract.image_to_string(img)
                image_url = img_path
                
    return render_template('index.html', ocr_text=ocr_text, image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)