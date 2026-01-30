# Módulos -> Utilizados pra expandir as funcionalidades do Python

# 1/3 -> Importação de módulos nativos
import os, time, sqlite3

print(os.name)

print("Primeira mensagem")
time.sleep(3)
print("Segunda mensagem")

# print(math.floor(3.2))
# print(math.ceil(3.2))

from math import ceil, floor

print(floor(3.2))
print(ceil(3.2))

# 2/3 -> Instalação de novos módulos pelo gerenciador de pacots do Python (PIP)

# pip install flask
# import flask

# 3/3 -> Instalação de módulos de terceiros

import modulos
modulos.saudacao("Tiago")

from modulos import saudacao
saudacao("tiago")

# Manipulaç±ao de arquivos python ===================

nome = input("Qual o seu nome? ")

# Modos mais comuns:
# a -> append (Acrescentar um conteudo sem apagar o que já existe)
# w -> write (Sobrescrever o conteudo atual do arquivo)
# r -> read (Ler o conteudo do arquivo)

arquivo = open("nomes.txt","a")
arquivo.write(f"Nome escolhido: {nome}\n")
arquivo.close()

arquivo2 = open("nomes.txt", "r")
conteudo = arquivo2.readlines()

for linha in conteudo:
    print(linha)

with open("nomes2.txt", "w") as arquivo3:
    arquivo3.write("Escrevendo o conteudo do arquivo")
    arquivo3.write("Escrevendo a segunda linha")

# Manipulando arquivos CSV
# common separated values

import csv

with open("planilha.csv") as arquivo:
    conteudo = csv.reader(arquivo, delimiter=";")

    for linha in conteudo:
        print(linha)
with open("planilha.csv", "w"):
    csv.write(arquivo)