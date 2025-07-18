from PIL import Image
import pytesseract
import pdf2image

def extract_text_from_file(file_path):
    if file_path.lower().endswith(".pdf"):
        images = pdf2image.convert_from_path(file_path)
        text = ""
        for img in images:
            text += pytesseract.image_to_string(img, lang="ara+fra") + "\n"
    else:
        img = Image.open(file_path)
        text = pytesseract.image_to_string(img, lang="ara+fra")
    return text
