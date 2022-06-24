import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from PIL import Image

#imagem original
image = Image.open('barras.png').convert('L')
image.show()


#espectro original
image_fourier = np.fft.fftshift(np.fft.fft2(image))
plt.figure(num=None, figsize=(8, 6), dpi=80)
plt.imshow(np.log(abs(image_fourier)), cmap='gray');


#6 rotações de 15 graus
for i in range(1,7):
    rot_image = image.rotate(15*i)
    rot_image.show()

    image_fourier = np.fft.fftshift(np.fft.fft2(rot_image))
    plt.figure(num=None, figsize=(8, 6), dpi=80)
    plt.imshow(np.log(abs(image_fourier)), cmap='gray');

#translação
#left 50px
a = 1 
b = 0
c = 50 #left/right
d = 0
e = 1
f = 0 #up/down
image_translation = image.transform(image.size, Image.AFFINE, (a, b, c, d, e, f))
image_translation.show()

image_fourier = np.fft.fftshift(np.fft.fft2(image_translation))
plt.figure(num=None, figsize=(8, 6), dpi=80)
plt.imshow(np.log(abs(image_fourier)), cmap='gray');

#down 50px
c = 0
f = -50
image_translation = image.transform(image.size, Image.AFFINE, (a, b, c, d, e, f))
image_translation.show()

image_fourier = np.fft.fftshift(np.fft.fft2(image_translation))
plt.figure(num=None, figsize=(8, 6), dpi=80)
plt.imshow(np.log(abs(image_fourier)), cmap='gray');

#escala
#2x size
width, height = image.size
zoomed_image = image.resize((width*2, height*2))
zoomed_image.show()

image_fourier = np.fft.fftshift(np.fft.fft2(zoomed_image))
plt.figure(num=None, figsize=(8, 6), dpi=80)
plt.imshow(np.log(abs(image_fourier)), cmap='gray')

#/2 size
zoomed_image = image.resize((int(width/2), int(height/2)))
zoomed_image.show()

image_fourier = np.fft.fftshift(np.fft.fft2(zoomed_image))
plt.figure(num=None, figsize=(8, 6), dpi=80)
plt.imshow(np.log(abs(image_fourier)), cmap='gray')

plt.show()