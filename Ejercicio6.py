# importing required modules
import math

import PyPDF2
import numpy as np

from matplotlib import pyplot as plt


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

frec11 = []
frec12 = []
frec13 = []
frec14 = []
frec15 = []
frec16 = []
frec17 = []
frec18 = []
frec19 = []
frec20 = []

benavides = []
# creating a pdf file object
pdfFileObj = open('benavides.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# creating a page object
for i in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(i)

# extracting text from page
    line = pageObj.extractText().lower()
    line = line.strip()
    line = line.split()
    for j in range(len(line)):
        if line[j] in stopwords:
            continue
        elif line[j] in doc1:
            benavides.append(line[j])
    #print(pageObj.extractText().lower())

# closing the pdf file object
pdfFileObj.close()
#print(benavides)

for i in doc1:
    count = benavides.count(i)
    frec11.append(count)
#print(frec11)


gomez = []
# creating a pdf file object
pdfFileObj = open('buendia.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# creating a page object
for i in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(i)

# extracting text from page
    line = pageObj.extractText().lower()
    line = line.strip()
    line = line.split()
    for j in range(len(line)):
        if line[j] in stopwords:
            continue
        elif line[j] in doc1:
            gomez.append(line[j])
    #print(pageObj.extractText().lower())

# closing the pdf file object
pdfFileObj.close()
#print(gomez)

for i in doc1:
    count = gomez.count(i)
    frec12.append(count)
#print(frec12)


jairala = []
# creating a pdf file object
pdfFileObj = open('corral.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# creating a page object
for i in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(i)

# extracting text from page
    line = pageObj.extractText().lower()
    line = line.strip()
    line = line.split()
    for j in range(len(line)):
        if line[j] in stopwords:
            continue
        elif line[j] in doc1:
            jairala.append(line[j])
    #print(pageObj.extractText().lower())

# closing the pdf file object
pdfFileObj.close()
#print(jairala)

for i in doc1:
    count = jairala.count(i)
    frec13.append(count)
#print(frec13)


jimenez = []
# creating a pdf file object
pdfFileObj = open('jacome.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# creating a page object
for i in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(i)

# extracting text from page
    line = pageObj.extractText().lower()
    line = line.strip()
    line = line.split()
    for j in range(len(line)):
        if line[j] in stopwords:
            continue
        elif line[j] in doc1:
            jimenez.append(line[j])
    #print(pageObj.extractText().lower())

# closing the pdf file object
pdfFileObj.close()
#print(jimenez)

for i in doc1:
    count = jimenez.count(i)
    frec14.append(count)
#print(frec14)


loro = []
# creating a pdf file object
pdfFileObj = open('yunda.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# creating a page object
for i in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(i)

# extracting text from page
    line = pageObj.extractText().lower()
    line = line.strip()
    line = line.split()
    for j in range(len(line)):
        if line[j] in stopwords:
            continue
        elif line[j] in doc1:
            loro.append(line[j])
    #print(pageObj.extractText().lower())

# closing the pdf file object
pdfFileObj.close()
#print(loro)

for i in doc1:
    count = loro.count(i)
    frec15.append(count)
#print(frec15)

maldonado = []
# creating a pdf file object
pdfFileObj = open('maldonado.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# creating a page object
for i in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(i)

# extracting text from page
    line = pageObj.extractText().lower()
    line = line.strip()
    line = line.split()
    for j in range(len(line)):
        if line[j] in stopwords:
            continue
        elif line[j] in doc1:
            maldonado.append(line[j])
    #print(pageObj.extractText().lower())

# closing the pdf file object
pdfFileObj.close()
#print(maldonado)

for i in doc1:
    count = maldonado.count(i)
    frec16.append(count)
#print(frec16)


rosero = []
# creating a pdf file object
pdfFileObj = open('vazquez.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# creating a page object
for i in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(i)

# extracting text from page
    line = pageObj.extractText().lower()
    line = line.strip()
    line = line.split()
    for j in range(len(line)):
        if line[j] in stopwords:
            continue
        elif line[j] in doc1:
            rosero.append(line[j])
    #print(pageObj.extractText().lower())

# closing the pdf file object
pdfFileObj.close()
#print(rosero)

for i in doc1:
    count = rosero.count(i)
    frec17.append(count)
#print(frec17)


ulloa = []
# creating a pdf file object
pdfFileObj = open('pasquel.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# creating a page object
for i in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(i)

# extracting text from page
    line = pageObj.extractText().lower()
    line = line.strip()
    line = line.split()
    for j in range(len(line)):
        if line[j] in stopwords:
            continue
        elif line[j] in doc1:
            ulloa.append(line[j])
    #print(pageObj.extractText().lower())

# closing the pdf file object
pdfFileObj.close()
#print(ulloa)

for i in doc1:
    count = ulloa.count(i)
    frec18.append(count)
#print(frec18)


vicky = []
# creating a pdf file object
pdfFileObj = open('moncayo.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# creating a page object
for i in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(i)

# extracting text from page
    line = pageObj.extractText().lower()
    line = line.strip()
    line = line.split()
    for j in range(len(line)):
        if line[j] in stopwords:
            continue
        elif line[j] in doc1:
            vicky.append(line[j])
    #print(pageObj.extractText().lower())

# closing the pdf file object
pdfFileObj.close()
#print(vicky)

for i in doc1:
    count = vicky.count(i)
    frec19.append(count)
#print(frec19)


viteri = []
# creating a pdf file object
pdfFileObj = open('vintimilla.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# creating a page object
for i in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(i)

# extracting text from page
    line = pageObj.extractText().lower()
    line = line.strip()
    line = line.split()
    for j in range(len(line)):
        if line[j] in stopwords:
            continue
        elif line[j] in doc1:
            viteri.append(line[j])
    #print(pageObj.extractText().lower())

# closing the pdf file object
pdfFileObj.close()
#print(viteri)

for i in doc1:
    count = viteri.count(i)
    frec20.append(count)
#print(frec20)

A = np.array([doc1, frec1, frec2, frec3, frec4, frec5, frec6, frec7, frec8, frec9, frec10, frec11, frec12, frec13, frec14, frec15, frec16, frec17, frec18, frec19, frec20])
A = A.T

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

#HOLAAAAA

aux = A[:,11]
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

aux = A[:,12]
cont = 0
col1 = []
for i in aux:
    square =int(i)**2
    cont += square
cont = math.sqrt(cont)
for i in aux:
    #col1.append(int(i)/cont)
    col1.append("{:.3f}".format(int(i) / cont))
A[:,12] = col1


aux = A[:,13]
cont = 0
col1 = []
for i in aux:
    square =int(i)**2
    cont += square
cont = math.sqrt(cont)
for i in aux:
    #col1.append(int(i)/cont)
    col1.append("{:.3f}".format(int(i) / cont))
A[:,13] = col1


aux = A[:,14]
cont = 0
col1 = []
for i in aux:
    square =int(i)**2
    cont += square
cont = math.sqrt(cont)
for i in aux:
    #col1.append(int(i)/cont)
    col1.append("{:.3f}".format(int(i) / cont))
A[:,14] = col1


aux = A[:,15]
cont = 0
col1 = []
for i in aux:
    square =int(i)**2
    cont += square
cont = math.sqrt(cont)
for i in aux:
    #col1.append(int(i)/cont)
    col1.append("{:.3f}".format(int(i) / cont))
A[:,15] = col1


aux = A[:,16]
cont = 0
col1 = []
for i in aux:
    square =int(i)**2
    cont += square
cont = math.sqrt(cont)
for i in aux:
    #col1.append(int(i)/cont)
    col1.append("{:.3f}".format(int(i) / cont))
A[:,16] = col1


aux = A[:,17]
cont = 0
col1 = []
for i in aux:
    square =int(i)**2
    cont += square
cont = math.sqrt(cont)
for i in aux:
    #col1.append(int(i)/cont)
    col1.append("{:.3f}".format(int(i) / cont))
A[:,17] = col1


aux = A[:,18]
cont = 0
col1 = []
for i in aux:
    square =int(i)**2
    cont += square
cont = math.sqrt(cont)
for i in aux:
    #col1.append(int(i)/cont)
    col1.append("{:.3f}".format(int(i) / cont))
A[:,18] = col1


aux = A[:,19]
cont = 0
col1 = []
for i in aux:
    square =int(i)**2
    cont += square
cont = math.sqrt(cont)
for i in aux:
    col1.append("{:.3f}".format(int(i)/cont))
A[:,19] = col1


aux = A[:,20]
cont = 0
col1 = []
for i in aux:
    square =int(i)**2
    cont += square
cont = math.sqrt(cont)
for i in aux:
    col1.append("{:.3f}".format(int(i)/cont))
A[:,20] = col1

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
planbenavides = np.array(A[:,11], dtype=float)
plangomez = np.array(A[:,12], dtype=float)
planjairala = np.array(A[:,13], dtype=float)
planjimenez = np.array(A[:,14], dtype=float)
planloro = np.array(A[:,15], dtype=float)
planmaldonado = np.array(A[:,16], dtype=float)
planrosero = np.array(A[:,17], dtype=float)
planulloa = np.array(A[:,18], dtype=float)
planvicky = np.array(A[:,19], dtype=float)
planviteri = np.array(A[:,20], dtype=float)

resultados['Benavides_Plan'] = np.dot(benavides, planbenavides)
resultados['Gomez_Plan'] = np.dot(gomez, plangomez)
resultados['Jairala_Plan'] = np.dot(jairala, planjairala)
resultados['Jimenez_Plan'] = np.dot(jimenez, planjimenez)
resultados['LoroHomero_Plan'] = np.dot(loro, planloro)
resultados['Maldonado_Plan'] = np.dot(maldonado, planmaldonado)
resultados['Rosero_Plan'] = np.dot(rosero, planrosero)
resultados['Ulloa_Plan'] = np.dot(ulloa, planulloa)
resultados['Vicky_Plan'] = np.dot(vicky, planvicky)
resultados['Viteri_Plan'] = np.dot(viteri, planviteri)

a = sorted(resultados.items(), key=lambda x: x[1], reverse=True)
print()

print("Candidatos que mas se desviaron:")
labels = []
data = []
for i in range(len(a)):
    cand, frecu = a[i]
    print("{:<20} {:<7} {:<7}".format(cand, ":", str(1-frecu)))
    labels.append(cand)
    data.append(1-frecu)

# Creating plot
fig = plt.figure(figsize=(10, 7))
plt.pie(data, labels=labels)

plt.title("Candidatos con mas desviacion")
# show plot
plt.show()

print()

data2 = []
print("Mejores relaciones de similaridad descendente:")
for i in range(len(a)):
    cand, frecu = a[i]
    print("{:<20} {:<7} {:<7}".format(cand, ":", str(frecu)))
    #labels.append(cand)
    data2.append(frecu)

# Creating plot
fig = plt.figure(figsize=(10, 7))
plt.pie(data2, labels=labels)

plt.title("Candidatos con mas similaridad")

# show plot
plt.show()
