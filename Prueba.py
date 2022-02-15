#EJERCICIO 2 Y 3
import csv
import time
import math
import matplotlib.pyplot as plt
from pip._internal.utils.misc import tabulate

x = ['Febrero', 'Marzo', 'Abril', 'Mayo']

ulloa = {}
benavides = {}
gomez = {}
jairala = {}
maldonado = {}
loroHomero = {}
vicky = {}
viteri = {}
jimenez = {}
rosero = {}

dfUlloa = {}
dfBenavides = {}
dfGomez = {}
dfJairala = {}
dfMaldonado = {}
dfLoro = {}
dfVicky = {}
dfViteri = {}
dfJimenez = {}
dfRosero = {}


ulloaFebrero = {}
benavidesFebrero = {}
gomezFebrero = {}
jairalaFebrero = {}
maldonadoFebrero = {}
loroHomeroFebrero = {}
vickyFebrero = {}
viteriFebrero = {}
jimenezFebrero= {}
roseroFebrero = {}


ulloaMarzo = {}
benavidesMarzo = {}
gomezMarzo = {}
jairalaMarzo = {}
maldonadoMarzo = {}
loroHomeroMarzo = {}
vickyMarzo = {}
viteriMarzo = {}
jimenezMarzo = {}
roseroMarzo = {}


ulloaAbril = {}
benavidesAbril = {}
gomezAbril = {}
jairalaAbril = {}
maldonadoAbril = {}
loroHomeroAbril = {}
vickyAbril = {}
viteriAbril = {}
jimenezAbril = {}
roseroAbril = {}


ulloaMayo = {}
benavidesMayo = {}
gomezMayo = {}
jairalaMayo = {}
maldonadoMayo = {}
loroHomeroMayo = {}
vickyMayo = {}
viteriMayo = {}
jimenezMayo = {}
roseroMayo = {}



top10_cand = []
stopwords = []
f = open("Top10_Candidatos.txt", "r")
for line in f:
    line = line.strip()
    top10_cand.append(line)
#print(top10_cand)
f.close()

f2 = open("Stopwords.txt", "r")
for linea in f2:
    linea = linea.strip()
    stopwords.append(linea)
#print(stopwords)
f2.close()

count = 0
count2 = 0
count3 = 0
#Empiezo a calcular el tf por candidato

#Archivo febrero
a1 = open("Tweet_Febrero.csv", encoding="utf8")
csvreader = csv.reader(a1)

for linea in csvreader:
    if len(linea) >= 3:
        if linea[2] == 'HernanUlloa':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') or palabra.__contains__('🇪🇨') :
                    continue
                elif palabra in ulloa.keys():
                    count = ulloa.get(palabra)
                    count += 1
                    ulloa[palabra] = count
                else:
                    ulloa[palabra] = 1
                if palabra in ulloaFebrero.keys():
                    count2 = ulloaFebrero.get(palabra)
                    count2 += 1
                    ulloaFebrero[palabra] = count2
                else:
                    ulloaFebrero[palabra] = 1
        if linea[2] == 'abenavidesgol1':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') or palabra.__contains__('🇪🇨') or palabra.__contains__('🎙') :
                    continue
                elif palabra in benavides.keys():
                    count = benavides.get(palabra)
                    count += 1
                    benavides[palabra] = count
                else:
                    benavides[palabra] = 1
                if palabra in benavidesFebrero.keys():
                    count2 = benavidesFebrero.get(palabra)
                    count2 += 1
                    benavidesFebrero[palabra] = count2
                else:
                    benavidesFebrero[palabra] = 1
        if linea[2] == 'wgomezr':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') or palabra.__contains__('🇪🇨') :
                    continue
                elif palabra in gomez.keys():
                    count = gomez.get(palabra)
                    count += 1
                    gomez[palabra] = count
                else:
                    gomez[palabra] = 1
                if palabra in gomezFebrero.keys():
                    count2 = gomezFebrero.get(palabra)
                    count2 += 1
                    gomezFebrero[palabra] = count2
                else:
                    gomezFebrero[palabra] = 1
        if linea[2] == 'jimmyjairala':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') or palabra.__contains__('🇪🇨') :
                    continue
                elif palabra in jairala.keys():
                    count = jairala.get(palabra)
                    count += 1
                    jairala[palabra] = count
                else:
                    jairala[palabra] = 1
                if palabra in jairalaFebrero.keys():
                    count2 = jairalaFebrero.get(palabra)
                    count2 += 1
                    jairalaFebrero[palabra] = count2
                else:
                    jairalaFebrero[palabra] = 1
        if linea[2] == 'LuisaMaldonadoM':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') or palabra.__contains__('🇪🇨') :
                    continue
                elif palabra in maldonado.keys():
                    count = maldonado.get(palabra)
                    count += 1
                    maldonado[palabra] = count
                else:
                    maldonado[palabra] = 1
                if palabra in maldonadoFebrero.keys():
                    count2 = maldonadoFebrero.get(palabra)
                    count2 += 1
                    maldonadoFebrero[palabra] = count2
                else:
                    maldonadoFebrero[palabra] = 1
        if linea[2] == 'LoroHomero':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') or palabra.__contains__('🇪🇨') :
                    continue
                elif palabra in loroHomero.keys():
                    count = loroHomero.get(palabra)
                    count += 1
                    loroHomero[palabra] = count
                else:
                    loroHomero[palabra] = 1
                if palabra in loroHomeroFebrero.keys():
                    count2 = loroHomeroFebrero.get(palabra)
                    count2 += 1
                    loroHomeroFebrero[palabra] = count2
                else:
                    ulloaFebrero[palabra] = 1
        if linea[2] == 'VickyDesintonio':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') or palabra.__contains__('🇪🇨') :
                    continue
                elif palabra in vicky.keys():
                    count = vicky.get(palabra)
                    count += 1
                    vicky[palabra] = count
                else:
                    vicky[palabra] = 1
                if palabra in vickyFebrero.keys():
                    count2 = vickyFebrero.get(palabra)
                    count2 += 1
                    vickyFebrero[palabra] = count2
                else:
                    vickyFebrero[palabra] = 1
        if linea[2] == 'CynthiaViteri6':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') or palabra.__contains__('🇪🇨') :
                    continue
                elif palabra in viteri.keys():
                    count = viteri.get(palabra)
                    count += 1
                    viteri[palabra] = count
                else:
                    viteri[palabra] = 1
                if palabra in viteriFebrero.keys():
                    count2 = viteriFebrero.get(palabra)
                    count2 += 1
                    viteriFebrero[palabra] = count2
                else:
                    viteriFebrero[palabra] = 1
        if linea[2] == 'fcojimenez21':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') or palabra.__contains__('🇪🇨') or palabra.__contains__('🗳') :
                    continue
                elif palabra in jimenez.keys():
                    count = jimenez.get(palabra)
                    count += 1
                    jimenez[palabra] = count
                else:
                    jimenez[palabra] = 1
                if palabra in jimenezFebrero.keys():
                    count2 = jimenezFebrero.get(palabra)
                    count2 += 1
                    jimenezFebrero[palabra] = count2
                else:
                    jimenezFebrero[palabra] = 1
        if linea[2] == 'davidroserow':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') or palabra.__contains__('🇪🇨') :
                    continue
                elif palabra in rosero.keys():
                    count = rosero.get(palabra)
                    count += 1
                    rosero[palabra] = count
                else:
                    rosero[palabra] = 1
                if palabra in roseroFebrero.keys():
                    count2 = roseroFebrero.get(palabra)
                    count2 += 1
                    roseroFebrero[palabra] = count2
                else:
                    roseroFebrero[palabra] = 1

#Archivo Marzo
a2 = open("Tweet_Marzo.csv", encoding="utf8")
csvreader = csv.reader(a2)

for linea in csvreader:
    if len(linea) >= 3:
        if linea[2] == 'HernanUlloa':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') or palabra.__contains__('🇪🇨') :
                    continue
                elif palabra in ulloa.keys():
                    count = ulloa.get(palabra)
                    count += 1
                    ulloa[palabra] = count
                else:
                    ulloa[palabra] = 1
                if palabra in ulloaMarzo.keys():
                    count2 = ulloaMarzo.get(palabra)
                    count2 += 1
                    ulloaMarzo[palabra] = count2
                else:
                    ulloaMarzo[palabra] = 1
        if linea[2] == 'abenavidesgol1':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') or palabra.__contains__('🎙') :
                    continue
                elif palabra in benavides.keys():
                    count = benavides.get(palabra)
                    count += 1
                    benavides[palabra] = count
                else:
                    benavides[palabra] = 1
                if palabra in benavidesMarzo.keys():
                    count2 = benavidesMarzo.get(palabra)
                    count2 += 1
                    benavidesMarzo[palabra] = count2
                else:
                    benavidesMarzo[palabra] = 1
        if linea[2] == 'wgomezr':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') :
                    continue
                elif palabra in gomez.keys():
                    count = gomez.get(palabra)
                    count += 1
                    gomez[palabra] = count
                else:
                    gomez[palabra] = 1
                if palabra in gomezMarzo.keys():
                    count2 = gomezMarzo.get(palabra)
                    count2 += 1
                    gomezMarzo[palabra] = count2
                else:
                    gomezMarzo[palabra] = 1
        if linea[2] == 'jimmyjairala':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') or palabra.__contains__('⤵️') :
                    continue
                elif palabra in jairala.keys():
                    count = jairala.get(palabra)
                    count += 1
                    jairala[palabra] = count
                else:
                    jairala[palabra] = 1
                if palabra in jairalaMarzo.keys():
                    count2 = jairalaMarzo.get(palabra)
                    count2 += 1
                    jairalaMarzo[palabra] = count2
                else:
                    jairalaMarzo[palabra] = 1
        if linea[2] == 'LuisaMaldonadoM':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') :
                    continue
                elif palabra in maldonado.keys():
                    count = maldonado.get(palabra)
                    count += 1
                    maldonado[palabra] = count
                else:
                    maldonado[palabra] = 1
                if palabra in maldonadoMarzo.keys():
                    count2 = maldonadoMarzo.get(palabra)
                    count2 += 1
                    maldonadoMarzo[palabra] = count2
                else:
                    maldonadoMarzo[palabra] = 1
        if linea[2] == 'LoroHomero':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') or palabra.__contains__('💙❤️❤️💙') :
                    continue
                elif palabra in loroHomero.keys():
                    count = loroHomero.get(palabra)
                    count += 1
                    loroHomero[palabra] = count
                else:
                    loroHomero[palabra] = 1
                if palabra in loroHomeroMarzo.keys():
                    count2 = loroHomeroMarzo.get(palabra)
                    count2 += 1
                    loroHomeroMarzo[palabra] = count2
                else:
                    loroHomeroMarzo[palabra] = 1
        if linea[2] == 'VickyDesintonio':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') :
                    continue
                elif palabra in vicky.keys():
                    count = vicky.get(palabra)
                    count += 1
                    vicky[palabra] = count
                else:
                    vicky[palabra] = 1
                if palabra in vickyMarzo.keys():
                    count2 = vickyMarzo.get(palabra)
                    count2 += 1
                    vickyMarzo[palabra] = count2
                else:
                    vickyMarzo[palabra] = 1
        if linea[2] == 'CynthiaViteri6':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') :
                    continue
                elif palabra in viteri.keys():
                    count = viteri.get(palabra)
                    count += 1
                    viteri[palabra] = count
                else:
                    viteri[palabra] = 1
                if palabra in viteriMarzo.keys():
                    count2 = viteriMarzo.get(palabra)
                    count2 += 1
                    viteriMarzo[palabra] = count2
                else:
                    viteriMarzo[palabra] = 1
        if linea[2] == 'fcojimenez21':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') or palabra.__contains__('🗳') :
                    continue
                elif palabra in jimenez.keys():
                    count = jimenez.get(palabra)
                    count += 1
                    jimenez[palabra] = count
                else:
                    jimenez[palabra] = 1
                if palabra in jimenezMarzo.keys():
                    count2 = jimenezMarzo.get(palabra)
                    count2 += 1
                    jimenezMarzo[palabra] = count2
                else:
                    jimenezMarzo[palabra] = 1
        if linea[2] == 'davidroserow':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') or palabra.__contains__('🇪🇨') :
                    continue
                elif palabra in rosero.keys():
                    count = rosero.get(palabra)
                    count += 1
                    rosero[palabra] = count
                else:
                    rosero[palabra] = 1
                if palabra in roseroMarzo.keys():
                    count2 = roseroMarzo.get(palabra)
                    count2 += 1
                    roseroMarzo[palabra] = count2
                else:
                    roseroMarzo[palabra] = 1

#Archivo Abril
a3 = open("Tweet_Abril.csv", encoding="utf8")
csvreader = csv.reader(a3)

for linea in csvreader:
    if len(linea) >= 3:
        if linea[2] == 'HernanUlloa':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') :
                    continue
                elif palabra in ulloa.keys():
                    count = ulloa.get(palabra)
                    count += 1
                    ulloa[palabra] = count
                else:
                    ulloa[palabra] = 1
                if palabra in ulloaAbril.keys():
                    count2 = ulloaAbril.get(palabra)
                    count2 += 1
                    ulloaAbril[palabra] = count2
                else:
                    ulloaAbril[palabra] = 1
        if linea[2] == 'abenavidesgol1':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') :
                    continue
                elif palabra in benavides.keys():
                    count = benavides.get(palabra)
                    count += 1
                    benavides[palabra] = count
                else:
                    benavides[palabra] = 1
                if palabra in benavidesAbril.keys():
                    count2 = benavidesAbril.get(palabra)
                    count2 += 1
                    benavidesAbril[palabra] = count2
                else:
                    benavidesAbril[palabra] = 1
        if linea[2] == 'wgomezr':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') :
                    continue
                elif palabra in gomez.keys():
                    count = gomez.get(palabra)
                    count += 1
                    gomez[palabra] = count
                else:
                    gomez[palabra] = 1
                if palabra in gomezAbril.keys():
                    count2 = gomezAbril.get(palabra)
                    count2 += 1
                    gomezAbril[palabra] = count2
                else:
                    gomezAbril[palabra] = 1
        if linea[2] == 'jimmyjairala':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') :
                    continue
                elif palabra in jairala.keys():
                    count = jairala.get(palabra)
                    count += 1
                    jairala[palabra] = count
                else:
                    jairala[palabra] = 1
                if palabra in jairalaAbril.keys():
                    count2 = jairalaAbril.get(palabra)
                    count2 += 1
                    jairalaAbril[palabra] = count2
                else:
                    jairalaAbril[palabra] = 1
        if linea[2] == 'LuisaMaldonadoM':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') :
                    continue
                elif palabra in maldonado.keys():
                    count = maldonado.get(palabra)
                    count += 1
                    maldonado[palabra] = count
                else:
                    maldonado[palabra] = 1
                if palabra in maldonadoAbril.keys():
                    count2 = maldonadoAbril.get(palabra)
                    count2 += 1
                    maldonadoAbril[palabra] = count2
                else:
                    maldonadoAbril[palabra] = 1
        if linea[2] == 'LoroHomero':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') :
                    continue
                elif palabra in loroHomero.keys():
                    count = loroHomero.get(palabra)
                    count += 1
                    loroHomero[palabra] = count
                else:
                    loroHomero[palabra] = 1
                if palabra in loroHomeroAbril.keys():
                    count2 = loroHomeroAbril.get(palabra)
                    count2 += 1
                    loroHomeroAbril[palabra] = count2
                else:
                    loroHomeroAbril[palabra] = 1
        if linea[2] == 'VickyDesintonio':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') or palabra.__contains__('||') :
                    continue
                elif palabra in vicky.keys():
                    count = vicky.get(palabra)
                    count += 1
                    vicky[palabra] = count
                else:
                    vicky[palabra] = 1
                if palabra in vickyAbril.keys():
                    count2 = vickyAbril.get(palabra)
                    count2 += 1
                    vickyAbril[palabra] = count2
                else:
                    vickyAbril[palabra] = 1
        if linea[2] == 'CynthiaViteri6':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') :
                    continue
                elif palabra in viteri.keys():
                    count = viteri.get(palabra)
                    count += 1
                    viteri[palabra] = count
                else:
                    viteri[palabra] = 1
                if palabra in viteriAbril.keys():
                    count2 = viteriAbril.get(palabra)
                    count2 += 1
                    viteriAbril[palabra] = count2
                else:
                    viteriAbril[palabra] = 1
        if linea[2] == 'fcojimenez21':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') or palabra.__contains__('🗳') :
                    continue
                elif palabra in jimenez.keys():
                    count = jimenez.get(palabra)
                    count += 1
                    jimenez[palabra] = count
                else:
                    jimenez[palabra] = 1
                if palabra in jimenezAbril.keys():
                    count2 = jimenezAbril.get(palabra)
                    count2 += 1
                    jimenezAbril[palabra] = count2
                else:
                    jimenezAbril[palabra] = 1
        if linea[2] == 'davidroserow':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') or palabra.__contains__('🇪🇨') :
                    continue
                elif palabra in rosero.keys():
                    count = rosero.get(palabra)
                    count += 1
                    rosero[palabra] = count
                else:
                    rosero[palabra] = 1
                if palabra in roseroAbril.keys():
                    count2 = roseroAbril.get(palabra)
                    count2 += 1
                    roseroAbril[palabra] = count2
                else:
                    roseroAbril[palabra] = 1

#Archivo Mayo
a4 = open("Tweet_Mayo.csv", encoding="utf8")
csvreader = csv.reader(a4)

for linea in csvreader:
    if len(linea) >= 3:
        if linea[2] == 'HernanUlloa':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') :
                    continue
                elif palabra in ulloa.keys():
                    count = ulloa.get(palabra)
                    count += 1
                    ulloa[palabra] = count
                else:
                    ulloa[palabra] = 1
                if palabra in ulloaMayo.keys():
                    count2 = ulloaMayo.get(palabra)
                    count2 += 1
                    ulloaMayo[palabra] = count2
                else:
                    ulloaMayo[palabra] = 1
        if linea[2] == 'abenavidesgol1':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') :
                    continue
                elif palabra in benavides.keys():
                    count = benavides.get(palabra)
                    count += 1
                    benavides[palabra] = count
                else:
                    benavides[palabra] = 1
                if palabra in benavidesMayo.keys():
                    count2 = benavidesMayo.get(palabra)
                    count2 += 1
                    benavidesMayo[palabra] = count2
                else:
                    benavidesMayo[palabra] = 1
        if linea[2] == 'wgomezr':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') :
                    continue
                elif palabra in gomez.keys():
                    count = gomez.get(palabra)
                    count += 1
                    gomez[palabra] = count
                else:
                    gomez[palabra] = 1
                if palabra in gomezMayo.keys():
                    count2 = gomezMayo.get(palabra)
                    count2 += 1
                    gomezMayo[palabra] = count2
                else:
                    gomezMayo[palabra] = 1
        if linea[2] == 'jimmyjairala':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') :
                    continue
                elif palabra in jairala.keys():
                    count = jairala.get(palabra)
                    count += 1
                    jairala[palabra] = count
                else:
                    jairala[palabra] = 1
                if palabra in jairalaMayo.keys():
                    count2 = jairalaMayo.get(palabra)
                    count2 += 1
                    jairalaMayo[palabra] = count2
                else:
                    jairalaMayo[palabra] = 1
        if linea[2] == 'LuisaMaldonadoM':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') :
                    continue
                elif palabra in maldonado.keys():
                    count = maldonado.get(palabra)
                    count += 1
                    maldonado[palabra] = count
                else:
                    maldonado[palabra] = 1
                if palabra in maldonadoMayo.keys():
                    count2 = maldonadoMayo.get(palabra)
                    count2 += 1
                    maldonadoMayo[palabra] = count2
                else:
                    maldonadoMayo[palabra] = 1
        if linea[2] == 'LoroHomero':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') :
                    continue
                elif palabra in loroHomero.keys():
                    count = loroHomero.get(palabra)
                    count += 1
                    loroHomero[palabra] = count
                else:
                    loroHomero[palabra] = 1
                if palabra in loroHomeroMayo.keys():
                    count2 = loroHomeroMayo.get(palabra)
                    count2 += 1
                    loroHomeroMayo[palabra] = count2
                else:
                    loroHomero[palabra] = 1
        if linea[2] == 'VickyDesintonio':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') or palabra.__contains__('||') :
                    continue
                elif palabra in vicky.keys():
                    count = vicky.get(palabra)
                    count += 1
                    vicky[palabra] = count
                else:
                    vicky[palabra] = 1
                if palabra in vickyMayo.keys():
                    count2 = vickyMayo.get(palabra)
                    count2 += 1
                    vickyMayo[palabra] = count2
                else:
                    vickyMayo[palabra] = 1
        if linea[2] == 'CynthiaViteri6':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') :
                    continue
                elif palabra in viteri.keys():
                    count = viteri.get(palabra)
                    count += 1
                    viteri[palabra] = count
                else:
                    viteri[palabra] = 1
                if palabra in viteriMayo.keys():
                    count2 = viteriMayo.get(palabra)
                    count2 += 1
                    viteriMayo[palabra] = count2
                else:
                    viteriMayo[palabra] = 1
        if linea[2] == 'fcojimenez21':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') or palabra.__contains__('🗳') :
                    continue
                elif palabra in jimenez.keys():
                    count = jimenez.get(palabra)
                    count += 1
                    jimenez[palabra] = count
                else:
                    jimenez[palabra] = 1
                if palabra in jimenezMayo.keys():
                    count2 = jimenezMayo.get(palabra)
                    count2 += 1
                    jimenezMayo[palabra] = count2
                else:
                    jimenezMayo[palabra] = 1
        if linea[2] == 'davidroserow':
            a = linea[3]
            a = a.lower()
            tw = a.split()
            #print(tw)
            for i in range(len(tw)):
                palabra = tw[i]
                if palabra in stopwords:
                    continue
                if palabra.__contains__('@') or palabra.__contains__('#') or palabra.__contains__('🇪🇨') :
                    continue
                elif palabra in rosero.keys():
                    count = rosero.get(palabra)
                    count += 1
                    rosero[palabra] = count
                else:
                    rosero[palabra] = 1
                if palabra in roseroMayo.keys():
                    count2 = roseroMayo.get(palabra)
                    count2 += 1
                    roseroMayo[palabra] = count2
                else:
                    roseroMayo[palabra] = 1


#Ulloa final
num = ulloa.get('candidatos')
num2 = ulloa.get('candidato')
num = num + num2
ulloa['candidato'] = num
del ulloa['candidatos']

num = ulloa.get('voto')
num2 = ulloa.get('votar')
num = num + num2
ulloa['voto'] = num
del ulloa['votar']

num = ulloa.get('ecuador')
num2 = ulloa.get('pais')
num = num + num2
ulloa['ecuador'] = num
del ulloa['pais']

arr = sorted(ulloa.items(), key=lambda x: x[1], reverse=True)
#print(arr)

#Benavides final

arr2 = sorted(benavides.items(), key=lambda x: x[1], reverse=True)
#print(arr2)

#Gomez final
num = gomez.get('voto')
num2 = gomez.get('vote')
num = num + num2
gomez['voto'] = num
del gomez['vote']

arr3 = sorted(gomez.items(), key=lambda x: x[1], reverse=True)
#print(arr3)

#Jairala final
num = jairala.get('guayaquil')
num2 = jairala.get('guayaquil.')
num = num + num2
jairala['guayaquil'] = num
del jairala['guayaquil.']

arr4 = sorted(jairala.items(), key=lambda x: x[1], reverse=True)
#print(arr4)

#Maldonando final
arr5 = sorted(maldonado.items(), key=lambda x: x[1], reverse=True)
#print(arr5)

#Loro Homero final
num = loroHomero.get('quito')
num2 = loroHomero.get('quito,')
num3 = loroHomero.get('quito.')
num = num + num2 + num3
loroHomero['quito'] = num
del loroHomero['quito,']
del loroHomero['quito.']
arr6 = sorted(loroHomero.items(), key=lambda x: x[1], reverse=True)
#print(arr6)

#Vicky final
num = vicky.get('ciudadanos')
num2 = vicky.get('ciudadana')
num = num + num2
vicky['ciudadanos'] = num
del vicky['ciudadana']
arr7 = sorted(vicky.items(), key=lambda x: x[1], reverse=True)
#print(arr7)

#Viteri final
num = viteri.get('guayaquil')
num2 = viteri.get('guayaquil!')
num3 = viteri.get('guayaquil.')
num = num + num2 + num3
viteri['guayaquil'] = num
del viteri['guayaquil!']
del viteri['guayaquil.']
arr8 = sorted(viteri.items(), key=lambda x: x[1], reverse=True)
#print(arr8)

#Jimenez final
num = jimenez.get('ciudad')
num2 = jimenez.get('ciudad.')
num = num + num2
jimenez['ciudad'] = num
del jimenez['ciudad.']
arr9 = sorted(jimenez.items(), key=lambda x: x[1], reverse=True)
#print(arr9)

#Rosero final
arr10 = sorted(rosero.items(), key=lambda x: x[1], reverse=True)
#print(arr5)

print("Top 10 palabras de Ulloa")
file3 = open("Top10_Ulloa.txt", "a")
for i in range(10):
    candidato, frecuencia = arr[i]
    y = []
    #print(candidato)
    if candidato in ulloaFebrero.keys():
        y.append(ulloaFebrero.get(candidato))
        if candidato in dfUlloa.keys():
            count3 = dfUlloa.get(candidato)
            count3 += 1
            dfUlloa[candidato] = count3
        else:
            dfUlloa[candidato] = 1
    else:
        y.append(0)
    if candidato in ulloaMarzo.keys():
        y.append(ulloaMarzo.get(candidato))
        if candidato in dfUlloa.keys():
            count3 = dfUlloa.get(candidato)
            count3 += 1
            dfUlloa[candidato] = count3
        else:
            dfUlloa[candidato] = 1
    else:
        y.append(0)
    if candidato in ulloaAbril.keys():
        y.append(ulloaAbril.get(candidato))
        if candidato in dfUlloa.keys():
            count3 = dfUlloa.get(candidato)
            count3 += 1
            dfUlloa[candidato] = count3
        else:
            dfUlloa[candidato] = 1
    else:
        y.append(0)
    if candidato in ulloaMayo.keys():
        y.append(ulloaMayo.get(candidato))
        if candidato in dfUlloa.keys():
            count3 = dfUlloa.get(candidato)
            count3 += 1
            dfUlloa[candidato] = count3
        else:
            dfUlloa[candidato] = 1
    else:
        y.append(0)
    df = dfUlloa.get(candidato)
    idf = math.log(4 / df, 10)
    tf_idf= frecuencia * idf
    #print(candidato + "\t" + ":" + "\t" + str(frecuencia) + "\t" + str(df))
    print("{:<15} {:<7} {:<7} {:<30} {:<15}".format(candidato, str(frecuencia), str(df), str(idf), str(tf_idf)))
    file3.write(candidato + "," + str(frecuencia) + "," + str(df) + "," + str(idf) + "," + str(tf_idf) + "\n")
    plt.plot(x, y, label=candidato)

plt.xlabel("Meses")
plt.ylabel("Frecuencia")
plt.title("Ulloa Top 10")
plt.legend()
plt.show()


time.sleep(5)
print()
print("Top 10 palabras de Benavides")
file4 = open("Top10_Benavides.txt", "a")
for i in range(10):
    candidato, frecuencia = arr2[i]
    y = []
    #print(candidato)
    if candidato in benavidesFebrero.keys():
        y.append(benavidesFebrero.get(candidato))
        if candidato in dfBenavides.keys():
            count3 = dfBenavides.get(candidato)
            count3 += 1
            dfBenavides[candidato] = count3
        else:
            dfBenavides[candidato] = 1
    else:
        y.append(0)
    if candidato in benavidesMarzo.keys():
        y.append(benavidesMarzo.get(candidato))
        if candidato in dfBenavides.keys():
            count3 = dfBenavides.get(candidato)
            count3 += 1
            dfBenavides[candidato] = count3
        else:
            dfBenavides[candidato] = 1
    else:
        y.append(0)
    if candidato in benavidesAbril.keys():
        y.append(benavidesAbril.get(candidato))
        if candidato in dfBenavides.keys():
            count3 = dfBenavides.get(candidato)
            count3 += 1
            dfBenavides[candidato] = count3
        else:
            dfBenavides[candidato] = 1
    else:
        y.append(0)
    if candidato in benavidesMayo.keys():
        y.append(benavidesMayo.get(candidato))
        if candidato in dfBenavides.keys():
            count3 = dfBenavides.get(candidato)
            count3 += 1
            dfBenavides[candidato] = count3
        else:
            dfBenavides[candidato] = 1
    else:
        y.append(0)
    df = dfBenavides.get(candidato)
    idf = math.log(4 / df, 10)
    #print(candidato + "\t" + ":" + "\t" + str(frecuencia) + "\t" + str(df))
    print("{:<15} {:<7} {:<7} {:<30} {:<15}".format(candidato, str(frecuencia), str(df), str(idf), str(tf_idf)))
    file4.write(candidato + "," + str(frecuencia) + "," + str(df) + "," + str(idf) + "," + str(tf_idf) + "\n")
    plt.plot(x, y, label=candidato)

plt.xlabel("Meses")
plt.ylabel("Frecuencia")
plt.title("Benavides Top 10")
plt.legend()
plt.show()

time.sleep(5)
print()
print("Top 10 palabras de Gomez")
file5 = open("Top10_Gomez.txt", "a")
for i in range(10):
    candidato, frecuencia = arr3[i]
    y=[]
    #print(candidato)
    if candidato in gomezFebrero.keys():
        y.append(gomezFebrero.get(candidato))
        if candidato in dfGomez.keys():
            count3 = dfGomez.get(candidato)
            count3 += 1
            dfGomez[candidato] = count3
        else:
            dfGomez[candidato] = 1
    else:
        y.append(0)
    if candidato in gomezMarzo.keys():
        y.append(gomezMarzo.get(candidato))
        if candidato in dfGomez.keys():
            count3 = dfGomez.get(candidato)
            count3 += 1
            dfGomez[candidato] = count3
        else:
            dfBenavides[candidato] = 1
    else:
        y.append(0)
    if candidato in gomezAbril.keys():
        y.append(gomezAbril.get(candidato))
        if candidato in dfGomez.keys():
            count3 = dfGomez.get(candidato)
            count3 += 1
            dfGomez[candidato] = count3
        else:
            dfGomez[candidato] = 1
    else:
        y.append(0)
    if candidato in gomezMayo.keys():
        y.append(gomezMayo.get(candidato))
        if candidato in dfGomez.keys():
            count3 = dfGomez.get(candidato)
            count3 += 1
            dfGomez[candidato] = count3
        else:
            dfGomez[candidato] = 1
    else:
        y.append(0)
    df = dfGomez.get(candidato)
    idf = math.log(4 / df, 10)
    #print(candidato + ":" + "\t" + str(frecuencia))
    print("{:<15} {:<7} {:<7} {:<30} {:<15}".format(candidato, str(frecuencia), str(df), str(idf), str(tf_idf)))
    file5.write(candidato + "," + str(frecuencia) + "," + str(df) + "," + str(idf) + "," + str(tf_idf) + "\n")
    plt.plot(x, y, label=candidato)

plt.xlabel("Meses")
plt.ylabel("Frecuencia")
plt.title("Gomez Top 10")
plt.legend()
plt.show()

time.sleep(5)
print()
print("Top 10 palabras de Jairala")
file6 = open("Top10_Jairala.txt", "a")
for i in range(10):
    candidato, frecuencia = arr4[i]
    y=[]
    #print(candidato)
    if candidato in jairalaFebrero.keys():
        y.append(jairalaFebrero.get(candidato))
        if candidato in dfJairala.keys():
            count3 = dfJairala.get(candidato)
            count3 += 1
            dfJairala[candidato] = count3
        else:
            dfJairala[candidato] = 1
    else:
        y.append(0)
    if candidato in jairalaMarzo.keys():
        y.append(jairalaMarzo.get(candidato))
        if candidato in dfJairala.keys():
            count3 = dfJairala.get(candidato)
            count3 += 1
            dfJairala[candidato] = count3
        else:
            dfJairala[candidato] = 1
    else:
        y.append(0)
    if candidato in jairalaAbril.keys():
        y.append(jairalaAbril.get(candidato))
        if candidato in dfJairala.keys():
            count3 = dfJairala.get(candidato)
            count3 += 1
            dfJairala[candidato] = count3
        else:
            dfJairala[candidato] = 1
    else:
        y.append(0)
    if candidato in jairalaMayo.keys():
        y.append(jairalaMayo.get(candidato))
        if candidato in dfJairala.keys():
            count3 = dfJairala.get(candidato)
            count3 += 1
            dfJairala[candidato] = count3
        else:
            dfJairala[candidato] = 1
    else:
        y.append(0)
    df = dfJairala.get(candidato)
    idf = math.log(4 / df, 10)
    #print(candidato + ":" + str(frecuencia))
    print("{:<15} {:<7} {:<7} {:<30} {:<15}".format(candidato, str(frecuencia), str(df), str(idf), str(tf_idf)))
    file6.write(candidato + "," + str(frecuencia) + "," + str(df) + "," + str(idf) + "," + str(tf_idf) + "\n")
    plt.plot(x, y, label=candidato)

plt.xlabel("Meses")
plt.ylabel("Frecuencia")
plt.title("Jairala Top 10")
plt.legend()
plt.show()


time.sleep(5)
print()
print("Top 10 palabras de Maldonado")
file7 = open("Top10_Maldonado.txt", "a")
for i in range(10):
    candidato, frecuencia = arr5[i]
    y=[]
    #print(candidato)
    if candidato in maldonadoFebrero.keys():
        y.append(maldonadoFebrero.get(candidato))
        if candidato in dfMaldonado.keys():
            count3 = dfMaldonado.get(candidato)
            count3 += 1
            dfMaldonado[candidato] = count3
        else:
            dfMaldonado[candidato] = 1
    else:
        y.append(0)
    if candidato in maldonadoMarzo.keys():
        y.append(maldonadoMarzo.get(candidato))
        if candidato in dfMaldonado.keys():
            count3 = dfMaldonado.get(candidato)
            count3 += 1
            dfMaldonado[candidato] = count3
        else:
            dfMaldonado[candidato] = 1
    else:
        y.append(0)
    if candidato in maldonadoAbril.keys():
        y.append(maldonadoAbril.get(candidato))
        if candidato in dfMaldonado.keys():
            count3 = dfMaldonado.get(candidato)
            count3 += 1
            dfMaldonado[candidato] = count3
        else:
            dfMaldonado[candidato] = 1
    else:
        y.append(0)
    if candidato in maldonadoMayo.keys():
        y.append(maldonadoMayo.get(candidato))
        if candidato in dfMaldonado.keys():
            count3 = dfMaldonado.get(candidato)
            count3 += 1
            dfMaldonado[candidato] = count3
        else:
            dfMaldonado[candidato] = 1
    else:
        y.append(0)
    df = dfMaldonado.get(candidato)
    idf = math.log(4 / df, 10)
    #print(candidato + ":" + str(frecuencia))
    print("{:<15} {:<7} {:<7} {:<30} {:<15}".format(candidato, str(frecuencia), str(df), str(idf), str(tf_idf)))
    file7.write(candidato + "," + str(frecuencia) + "," + str(df) + "," + str(idf) + "," + str(tf_idf) + "\n")
    plt.plot(x, y, label=candidato)

plt.xlabel("Meses")
plt.ylabel("Frecuencia")
plt.title("Maldonado Top 10")
plt.legend()
plt.show()

time.sleep(5)
print()
print("Top 10 palabras de LoroHomero")
file8 = open("Top10_LoroHomero.txt", "a")
for i in range(10):
    candidato, frecuencia = arr6[i]
    y=[]
    #print(candidato)
    if candidato in loroHomeroFebrero.keys():
        y.append(loroHomeroFebrero.get(candidato))
        if candidato in dfLoro.keys():
            count3 = dfLoro.get(candidato)
            count3 += 1
            dfLoro[candidato] = count3
        else:
            dfLoro[candidato] = 1
    else:
        y.append(0)
    if candidato in loroHomeroMarzo.keys():
        y.append(loroHomeroMarzo.get(candidato))
        if candidato in dfLoro.keys():
            count3 = dfLoro.get(candidato)
            count3 += 1
            dfLoro[candidato] = count3
        else:
            dfLoro[candidato] = 1
    else:
        y.append(0)
    if candidato in loroHomeroAbril.keys():
        y.append(loroHomeroAbril.get(candidato))
        if candidato in dfLoro.keys():
            count3 = dfLoro.get(candidato)
            count3 += 1
            dfLoro[candidato] = count3
        else:
            dfLoro[candidato] = 1
    else:
        y.append(0)
    if candidato in loroHomeroMayo.keys():
        y.append(loroHomeroMayo.get(candidato))
        if candidato in dfLoro.keys():
            count3 = dfLoro.get(candidato)
            count3 += 1
            dfLoro[candidato] = count3
        else:
            dfLoro[candidato] = 1
    else:
        y.append(0)
    df = dfLoro.get(candidato)
    idf = math.log(4 / df, 10)
    #print(candidato + ":" + str(frecuencia))
    print("{:<15} {:<7} {:<7} {:<30} {:<15}".format(candidato, str(frecuencia), str(df), str(idf), str(tf_idf)))
    file8.write(candidato + "," + str(frecuencia) + "," + str(df) + "," + str(idf) + "," + str(tf_idf) + "\n")
    plt.plot(x, y, label=candidato)

plt.xlabel("Meses")
plt.ylabel("Frecuencia")
plt.title("Loro Homero Top 10")
plt.legend()
plt.show()

time.sleep(5)
print()
print("Top 10 palabras de Vicky")
file9 = open("Top10_Vicky.txt", "a")
for i in range(10):
    candidato, frecuencia = arr7[i]
    y=[]
    #print(candidato)
    if candidato in vickyFebrero.keys():
        y.append(vickyFebrero.get(candidato))
        if candidato in dfVicky.keys():
            count3 = dfVicky.get(candidato)
            count3 += 1
            dfVicky[candidato] = count3
        else:
            dfVicky[candidato] = 1
    else:
        y.append(0)
    if candidato in vickyMarzo.keys():
        y.append(vickyMarzo.get(candidato))
        if candidato in dfVicky.keys():
            count3 = dfVicky.get(candidato)
            count3 += 1
            dfVicky[candidato] = count3
        else:
            dfVicky[candidato] = 1
    else:
        y.append(0)
    if candidato in vickyAbril.keys():
        y.append(vickyAbril.get(candidato))
        if candidato in dfVicky.keys():
            count3 = dfVicky.get(candidato)
            count3 += 1
            dfVicky[candidato] = count3
        else:
            dfVicky[candidato] = 1
    else:
        y.append(0)
    if candidato in vickyMayo.keys():
        y.append(vickyMayo.get(candidato))
        if candidato in dfVicky.keys():
            count3 = dfVicky.get(candidato)
            count3 += 1
            dfVicky[candidato] = count3
        else:
            dfVicky[candidato] = 1
    else:
        y.append(0)
    df = dfVicky.get(candidato)
    idf = math.log(4 / df, 10)
    #print(candidato + ":" + str(frecuencia))
    print("{:<15} {:<7} {:<7} {:<30} {:<15}".format(candidato, str(frecuencia), str(df), str(idf), str(tf_idf)))
    file9.write(candidato + "," + str(frecuencia) + "," + str(df) + "," + str(idf) + "," + str(tf_idf) + "\n")
    plt.plot(x, y, label=candidato)

plt.xlabel("Meses")
plt.ylabel("Frecuencia")
plt.title("Vicky Top 10")
plt.legend()
plt.show()

time.sleep(5)
print()
print("Top 10 palabras de Viteri")
file10 = open("Top10_Viteri.txt", "a")
for i in range(10):
    candidato, frecuencia = arr8[i]
    y=[]
    #print(candidato)
    if candidato in viteriFebrero.keys():
        y.append(viteriFebrero.get(candidato))
        if candidato in dfViteri.keys():
            count3 = dfViteri.get(candidato)
            count3 += 1
            dfViteri[candidato] = count3
        else:
            dfViteri[candidato] = 1
    else:
        y.append(0)
    if candidato in viteriMarzo.keys():
        y.append(viteriMarzo.get(candidato))
        if candidato in dfViteri.keys():
            count3 = dfViteri.get(candidato)
            count3 += 1
            dfViteri[candidato] = count3
        else:
            dfViteri[candidato] = 1
    else:
        y.append(0)
    if candidato in viteriAbril.keys():
        y.append(viteriAbril.get(candidato))
        if candidato in dfViteri.keys():
            count3 = dfViteri.get(candidato)
            count3 += 1
            dfViteri[candidato] = count3
        else:
            dfViteri[candidato] = 1
    else:
        y.append(0)
    if candidato in viteriMayo.keys():
        y.append(viteriMayo.get(candidato))
        if candidato in dfViteri.keys():
            count3 = dfViteri.get(candidato)
            count3 += 1
            dfViteri[candidato] = count3
        else:
            dfViteri[candidato] = 1
    else:
        y.append(0)
    df = dfViteri.get(candidato)
    idf = math.log(4 / df, 10)
    #print(candidato + ":" + str(frecuencia))
    print("{:<15} {:<7} {:<7} {:<30} {:<15}".format(candidato, str(frecuencia), str(df), str(idf), str(tf_idf)))
    file10.write(candidato + "," + str(frecuencia) + "," + str(df) + "," + str(idf) + "," + str(tf_idf) + "\n")
    plt.plot(x, y, label=candidato)

plt.xlabel("Meses")
plt.ylabel("Frecuencia")
plt.title("Viteri Top 10")
plt.legend()
plt.show()

time.sleep(5)
print()
print("Top 10 palabras de Jimenez")
file11 = open("Top10_Jimenez.txt", "a")
for i in range(10):
    candidato, frecuencia = arr9[i]
    y=[]
    #print(candidato)
    if candidato in jimenezFebrero.keys():
        y.append(jimenezFebrero.get(candidato))
        if candidato in dfJimenez.keys():
            count3 = dfJimenez.get(candidato)
            count3 += 1
            dfJimenez[candidato] = count3
        else:
            dfJimenez[candidato] = 1
    else:
        y.append(0)
    if candidato in jimenezMarzo.keys():
        y.append(jimenezMarzo.get(candidato))
        if candidato in dfJimenez.keys():
            count3 = dfJimenez.get(candidato)
            count3 += 1
            dfJimenez[candidato] = count3
        else:
            dfJimenez[candidato] = 1
    else:
        y.append(0)
    if candidato in jimenezAbril.keys():
        y.append(jimenezAbril.get(candidato))
        if candidato in dfJimenez.keys():
            count3 = dfJimenez.get(candidato)
            count3 += 1
            dfJimenez[candidato] = count3
        else:
            dfJimenez[candidato] = 1
    else:
        y.append(0)
    if candidato in jimenezMayo.keys():
        y.append(jimenezMayo.get(candidato))
        if candidato in dfJimenez.keys():
            count3 = dfJimenez.get(candidato)
            count3 += 1
            dfJimenez[candidato] = count3
        else:
            dfJimenez[candidato] = 1
    else:
        y.append(0)
    df = dfJimenez.get(candidato)
    idf = math.log(4 / df, 10)
    #print(candidato + ":" + str(frecuencia))
    print("{:<15} {:<7} {:<7} {:<30} {:<15}".format(candidato, str(frecuencia), str(df), str(idf), str(tf_idf)))
    file11.write(candidato + "," + str(frecuencia) + "," + str(df) + "," + str(idf) + "," + str(tf_idf) + "\n")
    plt.plot(x, y, label=candidato)

plt.xlabel("Meses")
plt.ylabel("Frecuencia")
plt.title("Jimenez Top 10")
plt.legend()
plt.show()

time.sleep(5)
print()
print("Top 10 palabras de Rosero")
file12 = open("Top10_Rosero.txt", "a")
for i in range(10):
    candidato, frecuencia = arr10[i]
    y=[]
    #print(candidato)
    if candidato in roseroFebrero.keys():
        y.append(roseroFebrero.get(candidato))
        if candidato in dfRosero.keys():
            count3 = dfRosero.get(candidato)
            count3 += 1
            dfRosero[candidato] = count3
        else:
            dfRosero[candidato] = 1
    else:
        y.append(0)
    if candidato in roseroMarzo.keys():
        y.append(roseroMarzo.get(candidato))
        if candidato in dfRosero.keys():
            count3 = dfRosero.get(candidato)
            count3 += 1
            dfRosero[candidato] = count3
        else:
            dfRosero[candidato] = 1
    else:
        y.append(0)
    if candidato in roseroAbril.keys():
        y.append(roseroAbril.get(candidato))
        if candidato in dfRosero.keys():
            count3 = dfRosero.get(candidato)
            count3 += 1
            dfRosero[candidato] = count3
        else:
            dfRosero[candidato] = 1
    else:
        y.append(0)
    if candidato in roseroMayo.keys():
        y.append(roseroMayo.get(candidato))
        if candidato in dfRosero.keys():
            count3 = dfRosero.get(candidato)
            count3 += 1
            dfRosero[candidato] = count3
        else:
            dfRosero[candidato] = 1
    else:
        y.append(0)
    df = dfRosero.get(candidato)
    idf = math.log(4 / df, 10)
    #print(candidato + ":" + str(frecuencia))
    print("{:<15} {:<7} {:<7} {:<30} {:<15}".format(candidato, str(frecuencia), str(df), str(idf), str(tf_idf)))
    file12.write(candidato + "," + str(frecuencia) + "," + str(df) + "," + str(idf) + "," + str(tf_idf) + "\n")
    plt.plot(x, y, label=candidato)

plt.xlabel("Meses")
plt.ylabel("Frecuencia")
plt.title("Rosero Top 10")
plt.legend()
plt.show()
