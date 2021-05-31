# -*-encoding:utf-8-*-
import pytesseract
from PIL import Image

# 测试的是pytesseract自带的图片，效果十分理想，完全没毛病
image = Image.open("test-european.jpg")
string = pytesseract.image_to_string(image)
print(string)
