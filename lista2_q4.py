#C) A equalização de contraste aplicada a cada canal de uma imagem colorida RGB resulta no surgimento de cores não presentes na imagem original, 
#isso ocorre porque os canais RGB são muito correlacionados. 
#
#Para o realce de uma imagem colorida, o ideal é lidar com um sistema de cor cujos componentes sejam menos correlacionados (mais independentes), 
#é o caso do sistema YIQ. I e Q são canais responsáveis pela pureza da cor, enquanto o canal Y é responsável pela luminosidade/brilho. 
#
#Nesse caso, apenas o canal de luminância (Y) é equalizado deixando os canais de crominância e (I e Q) inalterados. 
#Esse esquema é exibido na Figura 2. 
#
#Lembrando que a conversão de RGB ↔ YIQ pode ser realizada por métodos do pacote skimage: 
#• RGB → YIQ : skimage.color.rgb2yiq(rgb), 
#• YIQ → RGB : skimage.color.yiq2rgb(yiq)
#
#Para a imagem outono_LC.png: 
#i. Com a equalização de contraste que você implementou no item A, realize a equalização de contraste diretamente sobre os canais RGB da imagem; 
#ii. Realize a solução exibida na Figura 2, onde a etapa de Transformação baseada no histograma é realizada com a equalização de contraste 
#que você implementou no item A. 
#
#Sobre os resultados obtidos, exiba as imagens resultantes e compare os histogramas RGB com os histogramas YIQ antes e após as equalizações.

from skimage import io, color
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import histogram_equalizer as hteq
np.set_printoptions(threshold=np.inf)

image = Image.open('outono_LC.png')
image.show()

plt.figure(0)
histogram = image.histogram()
red_h = histogram[0:256]
green_h = histogram[256:512]
blue_h = histogram[512:768]

width = 0.25

for i in range(0, 256):
    plt.bar(i, red_h[i], +width, color = 'r')
for i in range(0, 256):
    plt.bar(i+width, green_h[i], +width, color = 'g')
for i in range(0, 256):
    plt.bar(i+width*2, blue_h[i], +width, color = 'b')

eq_image = hteq.hist_equalize_rgb(image, red_h, blue_h, green_h)

plt.figure(1)
new_histogram = eq_image.histogram()
n_red_h = new_histogram[0:256]
n_blue_h = new_histogram[256:512]
n_green_h = new_histogram[512:768]

width = 0.25

for i in range(0, 256):
    plt.bar(i, n_red_h[i], +width, color = 'r')
for i in range(0, 256):
    plt.bar(i+width, n_green_h[i], +width, color = 'g')
for i in range(0, 256):
    plt.bar(i+width*2, n_blue_h[i], +width, color = 'b')

eq_image.show()

height, width = image.size
size = height*width
yiq_image = color.rgb2yiq(image)
y_channel = yiq_image[:, :, 0]
y_channel_sorted = np.sort(y_channel.flatten())

y_hist, bins = np.histogram(y_channel.flatten())
cdf = y_hist.cumsum()
cdf = y_channel_sorted[-1] * cdf / cdf[-1]
y_eq = np.interp(y_channel.flatten(), bins[:-1], cdf)

y_eq = y_eq.reshape(y_channel.shape)
yiq_image[:, :, 0] = y_eq
rgb_image = color.yiq2rgb(yiq_image)
io.imsave("outono_yiq_equalizado.png", rgb_image)

plt.figure(2)
_ = plt.hist(rgb_image[:, :, 0].ravel(), bins = 256, color = 'red')
_ = plt.hist(rgb_image[:, :, 1].ravel(), bins = 256, color = 'Green')
_ = plt.hist(rgb_image[:, :, 2].ravel(), bins = 256, color = 'Blue')
plt.show()