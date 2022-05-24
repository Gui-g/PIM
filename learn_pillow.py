from enum import unique
from PIL import Image
import numpy as np
import itertools

#image = Image.open("colors.jpg")
#image.show()
#gray = image.convert('L')
#gray.show()

#image_r = Image.new('RGB', (100,100), (255,0,0))
#image_g = Image.new('RGB', (100,100), (0,255,0))
#image_b = Image.new('RGB', (100,100), (0,0,255))
#image_w = Image.new('RGB', (100,100), (255,255,255))

#def car_type(image_directory):
#    image = Image.open(image_directory)
#    r, g, b = image.getpixel((1,1))
#    if (r == 255) and (g == 255) and (b == 255):
#        return "white"
#    elif r == 255 and g == 0 and b == 0:
#        return "red"
#    elif r == 0 and g == 255 and b == 0:
#        return "green"
#    elif r == 0 and g == 0 and b == 255:
#        return "blue"
#    else:
#        return "error"


#image_r.show()
#r, g, b = image_r.getpixel((1,1))
#print(r, g, b)
#image_g.show()
#image_b.show()
#image_w.show()

np.set_printoptions(suppress=True)

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

point_list = [Point(650.7, 2000, 1500), Point(653.5, 2000, 1500), Point(650.7, 1990, 1500), Point(653.5, 1990, 1500), Point(645.3, 500.3, 1500), 
                  Point(645, 500.3, 1500), Point(645.3, 500, 1500), Point(645, 500, 1500)]

tabela_1 = [] #simulate tabela_1
for point in point_list:
    x, y, z = point.x, point.y, point.z
    tabela_1.append([x, y, z, 1])

#tabela_1 = [list(i) for i in zip(*tabela_1)] #transpose in list
tabela_1 = np.array(tabela_1)
tabela_1 = tabela_1.transpose()

focal_distance = 5

projection_map = np.array([[1,0,0,0], [0,1,0,0], [0,0,1/focal_distance,0]])

projection_w = np.matmul(projection_map, tabela_1)
w = projection_w[-1,]
projection_q = projection_w / w
projection_q = projection_q.transpose()

projected_points = []
for row in projection_q:
    projected_points.append(Point(row[0], row[1], row[2]))

def unique_pixel(point_a : Point, point_b : Point):
    if abs(point_a.x - point_b.x) <= 0.00075 and abs(point_a.x - point_b.x) != 0:
        print("pixel at position " + str(point_a.x) + " and pixel at position " + str(point_b.x) + " have only " + abs(point_a.x - point_b.x) + " distance and have merged")
        return 0 #same pixel
    elif abs(point_a.y - point_b.y) <= 0.00075 and abs(point_a.y - point_b.y) != 0:
        print("pixel at position " + str(point_a.y) + " and pixel at position " + str(point_b.y) + " have only " + abs(point_a.y - point_b.y) + " distance and have merged")
        return 0 #same pixel
    else:
        return 1 #unique pixel
    
for point_a, point_b in itertools.combinations(projected_points, 2):
    error = unique_pixel(point_a, point_b)

if error:
    print("all pixels are visible")

