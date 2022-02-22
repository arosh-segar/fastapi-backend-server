import pytesseract
from PIL import Image


def imgToText(image):
    im = Image.open(image)
    ocr_result = pytesseract.image_to_string(im)
    return ocr_result
