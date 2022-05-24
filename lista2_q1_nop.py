from PIL import Image, ImageOps

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

label = 50
def find_components(image : Image):
    bordered = ImageOps.expand(image, 1, 0)
    height, width = image.size
    labeled_image = Image.new('L', (height, width))

    width_range = range(1, width)
    height_range = range(1, height)

    for i in height_range:
        for j in width_range:
            window_labeler(bordered, labeled_image, label, i, j, 8)   

    return labeled_image 

def window_labeler(image : Image, label_image : Image, label, win_center_x, win_center_y, mode):
    if image.getpixel((win_center_x, win_center_y)) == 255:
        if label_image.getpixel((win_center_x, win_center_y)) == 0:
            label = label + 30
            label_image.putpixel((win_center_x, win_center_y), label)
        
        neighbors = newNeighborhood(win_center_x, win_center_y, mode)
        for neighbor in neighbors.neighbor_list:
            if image.getpixel((neighbor.x, neighbor.y)) == 255 and label_image.getpixel((neighbor.x, neighbor.y)) == 0:
                label_image.putpixel((neighbor.x, neighbor.y), label)