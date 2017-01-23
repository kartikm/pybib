from PIL import Image
import sys

import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

tool = tools[0]
langs = tool.get_available_languages()
lang = langs[1]

def digits(image_path, lang=None):
    return tool.image_to_string(
        Image.open(image_path),
        lang=lang,
        builder = pyocr.tesseract.DigitBuilder()
)

bib = digits('bib.png')

print("Bib number is: " + bib)
