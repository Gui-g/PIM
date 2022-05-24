import numpy as np

Matriz = np.array([[1,0,0,0], [0,1,0,0], [0,0,1/5,0]])

pontoA = np.array([[150.75], [1500.0], [500.0], [1.0]])
pontoB = np.array([[153.5], [1500], [500.0], [1.0]])
pontoC = np.array([[1500.0], [155.00], [500.0], [1.0]])
pontoD = np.array([[1500.0], [150.75], [500.0], [1.0]])
pontoE = np.array([[145.0], [153.0], [500.0], [1.0]])
pontoF = np.array([[144.3], [153.0], [500.0], [1.0]])

#coordenadas homogeneas
a_linha = Matriz.dot(pontoA)
b_linha = Matriz.dot(pontoB)
c_linha = Matriz.dot(pontoC)
d_linha = Matriz.dot(pontoD)
e_linha = Matriz.dot(pontoE)
f_linha = Matriz.dot(pontoF)

#novas coordenadas
a = a_linha / a_linha[2, 0]
print(a)
b = b_linha / b_linha[2, 0]
c = c_linha / c_linha[2, 0]
d = d_linha / d_linha[2, 0]
e = e_linha / e_linha[2, 0]
f = f_linha / f_linha[2, 0]

################################################
#Questão A

#Coordenadas
# A = [0, 1500, 500]
# B = [1500, 1500, 500]
# C = [0, 0, 500]
# D = [1500, 0, 500]
CA = 1500
CD = 1500
print(f'CA: {CA} | CD: {CD} | ABCD em mm: {CA * CD}') #o f faz com que a var seja substituida pelo valor que ela possui

################################################
#Questão B

print("A: ")
print(a)

print("B: ")
print(b)

print("C: ")
print(c)

print("D: ")
print(d)

print("E: ")
print(e)

print("F: ")
print(f)

################################################
#Questão C

dAB = abs(a - b)
dCD = abs(c - d)
dEF = abs(e - f)


if dAB[0, 0] > 0.0075:
    reg_ab = True
else:
    reg_ab = False

if dEF[0, 0] > 0.0075:
    reg_ef = True
else:
    reg_ef = False
    
if dCD[1, 0] > 0.0075:
    reg_cd = True
else:
    reg_cd = False

cont = 0

if reg_ab and reg_ef and reg_cd:
    cont = 3
    print("%d regioes" % cont)
elif reg_ab and reg_cd:
    cont = 2
    print("%d regioes - ACD e B" % cont)
elif reg_ab and reg_ef:
    cont = 2
    print("%d regioes - AC e BD" % cont)
else:
    cont = 1
    print("%d regiao" % cont)