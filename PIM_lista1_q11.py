from PIL import Image

image = Image.open("girassol.jpg")
# Gray
image = image.convert('L')
# Threshold
threshold1 = 100
threshold2 = 150
image = image.point( lambda p: 255 if p >= threshold1 and p <= threshold2 else 0 )
image.show()
# To mono
image = image.convert('1')