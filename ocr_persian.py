import pytesseract
from PIL import Image

# Install the Persian language pack
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
tessdata_dir_config = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata" -l fas'

# Load the image containing Persian text
image = Image.open('image.jpg')

# Extract the text from the image
text = pytesseract.image_to_string(image, lang='fas', config=tessdata_dir_config)

# Print the extracted text
print(text)