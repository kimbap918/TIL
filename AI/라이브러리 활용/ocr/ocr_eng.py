from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'
# print(pytesseract.image_to_string(Image.open('cnn_news.png')))

# print(pytesseract.image_to_string(Image.open('SOTA.png'), lang='eng+kor'))

print(pytesseract.image_to_string(Image.open('NEWS.png'), lang='eng+kor'))
