from datetime import datetime

from flask import Flask, render_template, request
import pytesseract
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

app = Flask(__name__, template_folder="template")


# Ana sayfayı yüklemek için GET isteği
@app.route('/')
def index():
    return render_template('/index.html')


# Dosya yüklemek için POST isteği
@app.route('/', methods=['POST'])
def upload():
    file = request.files['file']

    if file:
        filename = file.filename
        file.save(filename)
        extracted_text = ocr(filename)
        dosya = os.stat(filename)
        olusum = datetime.datetime.fromtimestamp(dosya.st_ctime)
        erisim = datetime.datetime.fromtimestamp(dosya.st_atime)
        degisim = datetime.datetime.fromtimestamp(dosya.st_mtime)
        boyut = f"{dosya.st_size}"
        dosya_adi = f"{filename}"
        erisim_tarihi = f"{erisim}"
        olusum_tarihi = f"{olusum}"
        degisim = f"{degisim}"

        os.remove(filename)
        return render_template('index.html', text=extracted_text)
                                dosya_olusum_tarihi = olusum_tarihi,
                                erisim_tarihi = erisim_tarihi,
                                degisim = degisim,
                                dosya_boyutu = boyut,
                                dosya_adi = dosya_adi )
    return render_template('index.html')


def ocr(filename):
    image = Image.open(filename)
    image.show()
    extracted_text = pytesseract.image_to_string(image)
    return extracted_text


if __name__ == '__main__':
    app.run(debug=True)
    app = Flask(__name__, template_folder="template")
