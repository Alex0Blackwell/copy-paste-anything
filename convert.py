import cv2
import pytesseract
import os
from PIL import Image


def getText():
    """ Get text from an image. """

    if(os.name == 'nt'):
        # is windows so tesseract must be specified
        pytesseract.pytesseract.tesseract_cmd = (
            r"C:\Program Files\Tesseract-OCR\tesseract"
        )

    image = cv2.imread('.capture.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # apply thresholding to preprocess the image
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # write the grayscale image to disk as a temporary file so we can apply OCR to it
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    # load the image as a PIL/Pillow image, apply OCR, and then delete the temporary file
    text = pytesseract.image_to_string(Image.open(filename))
    print(f"filename is {filename}")
    os.remove(filename)
    os.remove('.capture.png')
    return(text)
