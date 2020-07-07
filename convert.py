import cv2
import pytesseract


def getText():
    """ Get text from an image. """
    img = cv2.imread('.capture.png');
    return (pytesseract.image_to_string(img))
