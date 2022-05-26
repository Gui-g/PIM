#A) Implemente a função newNeighborhood(i,j,type) que a partir da localização (i,j) do
#centro de uma janela NxN (N ímpar), retorna os parâmetros para o acesso aos vizinhos
#de um pixel(i,j). Type é o tipo de vizinhança: vizinhança quatro ou vizinhança oito. Utilize
#esta função na implementação da segmentação por área via rotulação. A ideia é exibir a
#imagem de saída contendo apenas as circunferências contidas na imagem
#Teste_quads_circs_B.png bem como informar quantas circunferências ocorrem.

from PIL import Image, ImageOps
from collections import Counter

class Neighbor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Neighborhood:
    def __init__(self):
        self.neighbor_list = list()
    
    def set_new_neighbor(self, x, y):
        self.neighbor_list.append(Neighbor(x,y))

def newNeighborhood(i, j, type):
    neighborhood = Neighborhood()
    if type == 4:
        neighborhood.set_new_neighbor(i-1, j)
        neighborhood.set_new_neighbor(i, j-1)
        neighborhood.set_new_neighbor(i+1, j)
        neighborhood.set_new_neighbor(i, j+1)
    if type == 8:
        neighborhood.set_new_neighbor(i-1, j-1)
        neighborhood.set_new_neighbor(i-1, j)
        neighborhood.set_new_neighbor(i-1, j+1)
        neighborhood.set_new_neighbor(i, j-1)
        neighborhood.set_new_neighbor(i, j+1)
        neighborhood.set_new_neighbor(i+1, j-1)
        neighborhood.set_new_neighbor(i+1, j)
        neighborhood.set_new_neighbor(i+1, j+1)

    return neighborhood

def connected_component(image : Image):
    height, width = image.size
    bordered = ImageOps.expand(image, 1, 0) #creates 1px border
    return_img = Image.new('L', (height+1, width+1)) #creates image for labeling

    width_range = range(1, width)
    height_range = range(1, height)

    for i in height_range:
        for j in width_range:
            labeler(bordered, return_img, i, j, 8)

    return return_img

label = 50
def put_label(ret_img : Image, i, j, neighbor_x, neighbor_y):
    global label
    if ret_img.getpixel((neighbor_x, neighbor_y)) != 0:
        ret_img.putpixel((i, j), label) 
    if ret_img.getpixel((neighbor_x, neighbor_y)) == 0:
        label = label + 10
        ret_img.putpixel((i, j), label)

my_stack = list()
def labeler(og_img : Image, ret_img : Image, i, j, mode):
    if og_img.getpixel((i, j)) == 255 and ret_img.getpixel((i, j)) == 0:
        my_stack.append(tuple((i,j)))
        put_label(ret_img, i, j, i, j)
        while my_stack:
            i, j = my_stack.pop()
            neighbors = newNeighborhood(i, j, mode)
            for neighbor in neighbors.neighbor_list:
                if og_img.getpixel((neighbor.x, neighbor.y)) == 255 and ret_img.getpixel((neighbor.x, neighbor.y)) == 0:
                    my_stack.append(tuple((neighbor.x, neighbor.y)))
                    put_label(ret_img, neighbor.x, neighbor.y, i, j)

def find_objects(labeled_image : Image):
    label_list = list()
    height, width = labeled_image.size

    width_range = range(1, width-1)
    height_range = range(1, height-1)

    for i in width_range:
        for j in height_range:
            if labeled_image.getpixel((i, j)) != 0:
                label_list.append(labeled_image.getpixel((i,j)))
            
    count = Counter(label_list)
    count = count.most_common()
    return count

def find_smallest(pxl_list):
    smallest = 100000

    for element in pxl_list:
        if element[1] < smallest:
            smallest = element[1]
    
    return smallest

def filter_image(lbl_image : Image, pxl_list):

    labels_to_remove = list()
    small = find_smallest(pxl_list)
    for element in pxl_list:
        if element[1] != small:
            labels_to_remove.append(element[0])

    lbl_image = lbl_image.point(lambda p : 0 if p in labels_to_remove or p == 0 else 255)
    lbl_image.show()

image = Image.open("Teste_quadsCircs_B.png")
image = image.convert('L')
image.show()

threshold = 100
image = image.point(lambda p : 255 if p >= 100 else 0)
image = image.convert('1')

new_image = connected_component(image)
new_image.show()

obj_list = find_objects(new_image)

filter_image(new_image, obj_list)

#teste = numpy.asarray(new_image)
#for row in teste:
#    for val in row:
#        print(val, end = " ")
#    print