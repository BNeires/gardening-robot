import csv
import random  
from time import sleep

def csv_writer(data, path):
    with open(path, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
           writer.writerow(line)


def sensores():
  ID = random.choice(range(1))
  MES = random.choice(range(1,2))
  DIA = random.choice(range(0,24))
  HORA = random.choice(range(24))
  UMIDADE = random.choice(range(0,25))
  return "ID: %i; MES: %i; DIA: %i; Hora: %i; umidade: %i" % (ID,MES,DIA,HORA,UMIDADE)

def pre_processing(text):
 d = [] 
 dados = text.split("; ")
 for p in range(len(dados)):
    d.append(dados[p].split(":")[1])
 dados = [["ID", "MES", "DIA","Hora","umidade"],d]
 return dados


def gravar_dado(arquivo,text):
 with open(arquivo,'a') as log:
    while True:
        dados = pre_processing(text)
        writer = csv.writer(log,delimiter=",")
        writer.writerow(dados[1])       
        print dados[1]
        sleep(1)

while True:
 pre_dados = sensores()
 print pre_dados
 process = pre_processing(pre_dados)
 print process
 #gravar_dado("plantacao.csv",pre_processing(sensores()))
 #