#EJERCICIO 4
import math

import numpy as np

stopwords = []
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

f2 = open("Stopwords.txt", "r")
for linea in f2:
    linea = linea.strip()
    stopwords.append(linea)
#print(stopwords)
f2.close()

frec11 = np.array([0]*65)

A = np.array([doc1, frec1, frec2, frec3, frec4, frec5, frec6, frec7, frec8, frec9, frec10, frec11])
A = A.T
#print(A)

queryFinal = []
query = input("Escriba lo que desea buscar: ")
query = query.strip()
query = query.split()
for i in range(len(query)):
    if query[i] in stopwords:
        continue
    else:
        queryFinal.append(query[i])

#print(queryFinal)

auxiliar = []

for j in range(len(doc1)):
    word = doc1[j]
    if word in queryFinal:
        auxiliar.append(1)
    else:
        auxiliar.append(0)

print(auxiliar)
aux = auxiliar
cont = 0
col1 = []
for i in aux:
    square =int(i)**2
    cont += square
cont = math.sqrt(cont)
for i in aux:
    #col1.append(int(i)/cont)
    col1.append("{:.3f}".format(int(i) / cont))
A[:,11] = col1

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
query = np.array(A[:,11], dtype=float)

#print(np.dot(benavides, gomez))

resultados['Benavides'] = np.dot(benavides, query)
resultados['Gomez'] = np.dot(gomez, query)
resultados['Jairala'] = np.dot(jairala, query)
resultados['Jimenez'] = np.dot(jimenez, query)
resultados['LoroHomero'] = np.dot(loro, query)
resultados['Maldonado'] = np.dot(maldonado, query)
resultados['Rosero'] = np.dot(rosero, query)
resultados['Ulloa'] = np.dot(ulloa, query)
resultados['Vicky'] = np.dot(vicky, query)
resultados['Viteri'] = np.dot(viteri, query)

a = sorted(resultados.items(), key=lambda x: x[1], reverse=True)
print()
print("Mejores relaciones de similaridad descendente:")
for i in range(len(a)):
    cand, frecu = a[i]
    print("{:<20} {:<7} {:<7}".format(cand, ":", str(frecu)))






