import os
import pytesseract as pt
from PIL import Image

WINDOWS = "nt"


def get_text(image: Image) -> str:
    """
    Get text from a provided image.

    :param image    The image to extract text from
    :returns:       The text from the image
    """
    if os.name == WINDOWS:
        # pytesseract must be specified on Windows
        pt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"

    text_from_image = pt.image_to_string(image)
    return text_from_image.strip()
