import pytesseract
from PIL import Image


def imgToText(image):
    pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'
    im = Image.open(image)
    ocr_result = pytesseract.image_to_string(im)
    return ocr_result
