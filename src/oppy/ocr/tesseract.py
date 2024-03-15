import pytesseract
from oppy.img.process import Image


TESSERACT_DPI_TRESHOLD = 300


def ocr(image: Image, lang: str) -> str:
    return pytesseract.image_to_string(image.image, lang=lang)