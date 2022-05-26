#A) Implemente o algoritmo de equalização de histograma descrito no pdf “operações
#sobre pixels”. Aplique a sua implementação sobre a imagem gonzalezWoods_3_10.png e
#marilyn.jpg contida na pasta de imagens para testes. Compare os histogramas anterior e
#posterior à equalização quanto a distribuição de frequências dos tons de cinza. 

from turtle import color
from PIL import Image
import matplotlib.pyplot as plt
import histogram_equalizar as hteq

image = Image.open('gonzalezWoods_3_10.png').convert('L')
image.show()
width, height = image.size
size = width*height

histogram = image.histogram()

plt.figure(0)
for i in range(len(histogram)):
    plt.bar(i, histogram[i], color = (0,0,0))

equalized_map = hteq.equalize_hist(histogram, size)
new_image = image.point(lambda p : hteq.pxl_map_eq_hist(p, equalized_map))

new_hist = new_image.histogram()
plt.figure(1)
for i in range(len(new_hist)):
    plt.bar(i, new_hist[i], color = (0,0,0))
new_image.show()
plt.show()