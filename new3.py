#EJERCICIO 5
import math

import numpy as np
d1 = {}
d2 = {}
d3 = {}
d4 = {}
d5 = {}
d6 = {}
d7 = {}
d8 = {}
d9 = {}
d10 = {}

frec1 = []
frec2 = []
frec3 = []
frec4 = []
frec5 = []
frec6 = []
frec7 = []
frec8 = []
frec9 = []
frec10 = []
doc1 = []

file = open("Top10_Benavides.txt", "r")
for linea in file:
    linea = linea.strip()
    linea = linea.split(",")
    doc1.append(linea[0])
    d1[linea[0]] = linea[1]
    # frec1.append(line[1])

file2 = open("Top10_Gomez.txt", "r")
for line in file2:
    line = line.strip()
    line = line.split(",")
    d2[line[0]] = line[1]
    if line[0] not in doc1:
        doc1.append(line[0])
        # frec1.append(line[1])

file3 = open("Top10_Jairala.txt", "r")
for line in file3:
    line = line.strip()
    line = line.split(",")
    d3[line[0]] = line[1]
    if line[0] not in doc1:
        doc1.append(line[0])
        # frec1.append(line[1])

file4 = open("Top10_Jimenez.txt", "r")
for line in file4:
    line = line.strip()
    line = line.split(",")
    d4[line[0]] = line[1]
    if line[0] not in doc1:
        doc1.append(line[0])
        # frec1.append(line[1])

file5 = open("Top10_LoroHomero.txt", "r")
for line in file5:
    line = line.strip()
    line = line.split(",")
    d5[line[0]] = line[1]
    if line[0] not in doc1:
        doc1.append(line[0])

file6 = open("Top10_Maldonado.txt", "r")
for line in file6:
    line = line.strip()
    line = line.split(",")
    d6[line[0]] = line[1]
    if line[0] not in doc1:
        doc1.append(line[0])

file7 = open("Top10_Rosero.txt", "r")
for line in file7:
    line = line.strip()
    line = line.split(",")
    d7[line[0]] = line[1]
    if line[0] not in doc1:
        doc1.append(line[0])

file8 = open("Top10_Ulloa.txt", "r")
for line in file8:
    line = line.strip()
    line = line.split(",")
    d8[line[0]] = line[1]
    if line[0] not in doc1:
        doc1.append(line[0])

file9 = open("Top10_Vicky.txt", "r")
for line in file9:
    line = line.strip()
    line = line.split(",")
    d9[line[0]] = line[1]
    if line[0] not in doc1:
        doc1.append(line[0])

file10 = open("Top10_Viteri.txt", "r")
for line in file10:
    line = line.strip()
    line = line.split(",")
    d10[line[0]] = line[1]
    if line[0] not in doc1:
        doc1.append(line[0])

for i in doc1:
    if i in d1.keys():
        frec1.append(d1.get(i))
    else:
        frec1.append(0)

for a in doc1:
    if a in d2.keys():
        frec2.append(d2.get(a))
    else:
        frec2.append(0)

for i in doc1:
    if i in d3.keys():
        frec3.append(d3.get(i))
    else:
        frec3.append(0)

for i in doc1:
    if i in d4.keys():
        frec4.append(d4.get(i))
    else:
        frec4.append(0)

for i in doc1:
    if i in d5.keys():
        frec5.append(d5.get(i))
    else:
        frec5.append(0)

for i in doc1:
    if i in d6.keys():
        frec6.append(d6.get(i))
    else:
        frec6.append(0)

for i in doc1:
    if i in d7.keys():
        frec7.append(d7.get(i))
    else:
        frec7.append(0)

for i in doc1:
    if i in d8.keys():
        frec8.append(d8.get(i))
    else:
        frec8.append(0)

for i in doc1:
    if i in d9.keys():
        frec9.append(d9.get(i))
    else:
        frec9.append(0)

for i in doc1:
    if i in d10.keys():
        frec10.append(d10.get(i))
    else:
        frec10.append(0)



A = np.array([doc1, frec1, frec2, frec3, frec4, frec5, frec6, frec7, frec8, frec9, frec10])
A = A.T
print(A)

aux = A[:,1]
cont = 0
col1 = []
for i in aux:
    square =int(i)**2
    cont += square
cont = math.sqrt(cont)
for i in aux:
    #col1.append(int(i)/cont)
    col1.append("{:.3f}".format(int(i) / cont))
A[:,1] = col1

aux = A[:,2]
cont = 0
col1 = []
for i in aux:
    square =int(i)**2
    cont += square
cont = math.sqrt(cont)
for i in aux:
    #col1.append(int(i)/cont)
    col1.append("{:.3f}".format(int(i) / cont))
A[:,2] = col1


aux = A[:,3]
cont = 0
col1 = []
for i in aux:
    square =int(i)**2
    cont += square
cont = math.sqrt(cont)
for i in aux:
    #col1.append(int(i)/cont)
    col1.append("{:.3f}".format(int(i) / cont))
A[:,3] = col1


aux = A[:,4]
cont = 0
col1 = []
for i in aux:
    square =int(i)**2
    cont += square
cont = math.sqrt(cont)
for i in aux:
    #col1.append(int(i)/cont)
    col1.append("{:.3f}".format(int(i) / cont))
A[:,4] = col1


aux = A[:,5]
cont = 0
col1 = []
for i in aux:
    square =int(i)**2
    cont += square
cont = math.sqrt(cont)
for i in aux:
    #col1.append(int(i)/cont)
    col1.append("{:.3f}".format(int(i) / cont))
A[:,5] = col1


aux = A[:,6]
cont = 0
col1 = []
for i in aux:
    square =int(i)**2
    cont += square
cont = math.sqrt(cont)
for i in aux:
    #col1.append(int(i)/cont)
    col1.append("{:.3f}".format(int(i) / cont))
A[:,6] = col1


aux = A[:,7]
cont = 0
col1 = []
for i in aux:
    square =int(i)**2
    cont += square
cont = math.sqrt(cont)
for i in aux:
    #col1.append(int(i)/cont)
    col1.append("{:.3f}".format(int(i) / cont))
A[:,7] = col1


aux = A[:,8]
cont = 0
col1 = []
for i in aux:
    square =int(i)**2
    cont += square
cont = math.sqrt(cont)
for i in aux:
    #col1.append(int(i)/cont)
    col1.append("{:.3f}".format(int(i) / cont))
A[:,8] = col1


aux = A[:,9]
cont = 0
col1 = []
for i in aux:
    square =int(i)**2
    cont += square
cont = math.sqrt(cont)
for i in aux:
    col1.append("{:.3f}".format(int(i)/cont))
A[:,9] = col1


aux = A[:,10]
cont = 0
col1 = []
for i in aux:
    square =int(i)**2
    cont += square
cont = math.sqrt(cont)
for i in aux:
    col1.append("{:.3f}".format(int(i)/cont))
A[:,10] = col1

print("NUEVA MATRIZ")
print(A)

resultados = {}

benavides = np.array(A[:,1], dtype=float)
gomez = np.array(A[:,2], dtype=float)
jairala = np.array(A[:,3], dtype=float)
jimenez = np.array(A[:,4], dtype=float)
loro = np.array(A[:,5], dtype=float)
maldonado = np.array(A[:,6], dtype=float)
rosero = np.array(A[:,7], dtype=float)
ulloa = np.array(A[:,8], dtype=float)
vicky = np.array(A[:,9], dtype=float)
viteri = np.array(A[:,10], dtype=float)

#print(np.dot(benavides, gomez))

resultados['Benavides_Gomez'] = np.dot(benavides, gomez)
resultados['Benavides_Jairala'] = np.dot(benavides, jairala)
resultados['Benavides_Jimenez'] = np.dot(benavides, jimenez)
resultados['Benavides_LoroHomero'] = np.dot(benavides, loro)
resultados['Benavides_Maldonado'] = np.dot(benavides, maldonado)
resultados['Benavides_Rosero'] = np.dot(benavides, rosero)
resultados['Benavides_Ulloa'] = np.dot(benavides, ulloa)
resultados['Benavides_Vicky'] = np.dot(benavides, vicky)
resultados['Benavides_Viteri'] = np.dot(benavides, viteri)

resultados['Gomez_Jairala'] = np.dot(gomez, jairala)
resultados['Gomez_Jimenez'] = np.dot(gomez, jimenez)
resultados['Gomez_LoroHomero'] = np.dot(gomez, loro)
resultados['Gomez_Maldonado'] = np.dot(gomez, maldonado)
resultados['Gomez_Rosero'] = np.dot(gomez, rosero)
resultados['Gomez_Ulloa'] = np.dot(gomez, ulloa)
resultados['Gomez_Vicky'] = np.dot(gomez, vicky)
resultados['Gomez_Viteri'] = np.dot(gomez, viteri)

resultados['Jairala_Jimenez'] = np.dot(jairala, jimenez)
resultados['Jairala_LoroHomero'] = np.dot(jairala, loro)
resultados['Jairala_Maldonado'] = np.dot(jairala, maldonado)
resultados['Jairala_Rosero'] = np.dot(jairala, rosero)
resultados['Jairala_Ulloa'] = np.dot(jairala, ulloa)
resultados['Jairala_Vicky'] = np.dot(jairala, vicky)
resultados['Jairala_Viteri'] = np.dot(jairala, viteri)

resultados['Jimenez_LoroHomero'] = np.dot(jimenez, loro)
resultados['Jimenez_Maldonado'] = np.dot(jimenez, maldonado)
resultados['Jimenez_Rosero'] = np.dot(jimenez, rosero)
resultados['Jimenez_Ulloa'] = np.dot(jimenez, ulloa)
resultados['Jimenez_Vicky'] = np.dot(jimenez, vicky)
resultados['Jimenez_Viteri'] = np.dot(jimenez, viteri)

resultados['LoroHomero_Maldonado'] = np.dot(loro, maldonado)
resultados['LoroHomero_Rosero'] = np.dot(loro, rosero)
resultados['LoroHomero_Ulloa'] = np.dot(loro, ulloa)
resultados['LoroHomero_Vicky'] = np.dot(loro, vicky)
resultados['LoroHomero_Viteri'] = np.dot(loro, viteri)

resultados['Maldonado_Rosero'] = np.dot(maldonado, rosero)
resultados['Maldonado_Ulloa'] = np.dot(maldonado, ulloa)
resultados['Maldonado_Vicky'] = np.dot(maldonado, vicky)
resultados['Maldonado_Viteri'] = np.dot(maldonado, viteri)

resultados['Rosero_Ulloa'] = np.dot(rosero, ulloa)
resultados['Rosero_Vicky'] = np.dot(rosero, vicky)
resultados['Rosero_Viteri'] = np.dot(rosero, viteri)

resultados['Ulloa_Vicky'] = np.dot(ulloa, vicky)
resultados['Ulloa_Viteri'] = np.dot(ulloa, viteri)

resultados['Vicky_Viteri'] = np.dot(vicky, viteri)

a = sorted(resultados.items(), key=lambda x: x[1], reverse=True)
print()
print("Mejores relaciones de similaridad descendente:")
for i in range(len(a)):
    cand, frecu = a[i]
    print("{:<20} {:<7} {:<7}".format(cand, ":", str(frecu)))






