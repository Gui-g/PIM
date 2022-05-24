import numpy as np
import itertools

np.set_printoptions(suppress=True)

class Point:
    def __init__(self, x, y, z):
        self.name = ''
        self.x = x
        self.y = y
        self.z = z

    def set_name(self, name):
        self.name = name

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
for i in range(len(projected_points)):
    projected_points[i].set_name(chr(i+65))

def unique_pixel(point_a : Point, point_b : Point):
    if np.sqrt(np.power(point_b.x - point_a.x, 2) + np.power(point_b.y - point_a.y,2)) <= 0.0075 : #test distance
        print("point " + str(point_a.name) + " and point " + str(point_b.name) + " have only " + str(np.sqrt(np.power(point_b.x - point_a.x, 2) + np.power(point_b.y - point_a.y,2))) + " distance and have merged")
        return 0 #same pixel
    else:
        print("unique pair " + str(point_a.name) + " and " + str(point_b.name))
        return 1 #unique pixel
    
for point_a, point_b in itertools.combinations(projected_points, 2):
    success = unique_pixel(point_a, point_b)

if success:
    print("-----------------------")
    print("all pixels are visible")
