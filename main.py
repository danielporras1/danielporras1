#EJERCICIO 1
import csv
import time

accountsCandidate = {}
top10_cand = []

file = open("account_info.csv", "r")
for linea in file:
    linea = linea.strip()
    info = linea.split(",")
    element = info[6]
    accountsCandidate[element] = 0
#print(accountsCandidate)

file.close()

file2 = open("livetweets_data_no_json.csv", encoding="utf8")
for linea2 in file2:
    linea2 = linea2.strip()
    info2 = linea2.split(",")
    if len(info2) >= 3:
        screenName = info2[2]
        if screenName in accountsCandidate:
            count = accountsCandidate.get(screenName)
            count += 1
            accountsCandidate[screenName] = count
#print(accountsCandidate)
a = sorted(accountsCandidate.items(), key=lambda x: x[1], reverse=True)
print("Top 10 Candidatos que mas usaron Twitter:")
for i in range(10):
    cand, frec = a[i]
    print(cand + ": " + str(frec))
file2.close()

file3 = open("Top10_Candidatos.txt", "a")
for i in range(10):
    candidato, frecuencia = a[i]
    #print(candidato)
    top10_cand.append(candidato)
    file3.write(candidato + "\n")
file3.close()

time.sleep(5)


f3 = open("Tweet_Febrero.csv", "a", encoding='UTF8')
f4 = open("Tweet_Marzo.csv", "a", encoding='UTF8')
f5 = open("Tweet_Abril.csv", "a", encoding='UTF8')
f6 = open("Tweet_Mayo.csv", "a", encoding='UTF8')

file = open("livetweets_data_no_json.csv", encoding="utf8")
csvreader = csv.reader(file)
rows = []
for row in csvreader:
    if len(row) >= 3:
        if row[2] in top10_cand:
            aux = row[1].split("-")
            #print(aux)
            if aux[1] == "02":
                writer = csv.writer(f3)
                writer.writerow(row)
            if aux[1] == "03":
                writer = csv.writer(f4)
                writer.writerow(row)
            if aux[1] == "04":
                writer = csv.writer(f5)
                writer.writerow(row)
            if aux[1] == "05":
                writer = csv.writer(f6)
                writer.writerow(row)
file.close()
f3.close()
f4.close()
f5.close()
f6.close()