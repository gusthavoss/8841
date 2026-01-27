# # Estruturas de repetição (WHILE e FOR)

# # While (Enquanto) ===========

# Variavel de controle:
contador = 10

while contador > 0:
    print(f"O valor do contador atualmente é {contador}")
    contador = contador - 1

# # While True:

while True:
    resposta = input("Voce quer parar este loop? [S/N]: ")
    if resposta == "S":
        break

# continue:

numeral = 1
while True:
    resposta = input("Voce quer ver o valor atual da variavel numeral? [s/n]: ")
    if resposta != "s":
        continue
    print(numeral)
    numeral += 1 # faz o mesmo que numeral = numeral + 1
    break

# FOR (para) ===================
numero = 0
for numero in range(0, 71):
    print(f"Valor atual da variavel do for: {numero}")

nome = "Tiago"

for letra in nome:
    print(letra)

# Coleções =====================

# Tuplas / Listas / Dicionários / Sets

#Tuplas
# Tuplas são coleções de objetos no python que não podem ser alteradas.

tupla = (45, 111, True, "Ghus", "Kaina", 96.3) # Tuplas são criadas com parentesis
# INDEX  0    1     2     3        4      5

print(tupla)
print(tupla[3])

for objeto in tupla:
    print(f"Valor recebido pela variavel do for vindo da tupla {objeto}")

#LISTAS
# Listas são muito semelhantes à tuplas, porem são bem mais flexiveis.

lista = [23, 55, false, "Roberto", "Alessandra", 85.663, tupla] # Listas são criadas com colchetes
# INDEX.  1   2.   3.       4.           5.         6

print(lista)
print(lista[5])
print(lista[6][2])

lista.append(True)
print(lista)

lista.insert(2, "Novo nome")
print(lista)

lista.pop(1)
print(lista)

posicao = lista.index("Alessandra")
print(posicao)

# DICIONÁRIOS -------------
# Dicionários são coleções estruturadas em pares de {"Chave": "Valor"}

#                 ITEM             ITEM          ITEM               ITEM
dicionario = {"Nome":"Tiago", "Idade": 29, "Altura": 1.89, "Masculino": True}
#              CHAVE: VALOR.    CHAVE: VALOR.  CHAVE: VALOR.     CHAVE: VALOR

# Chaves em dicionários são UNICAS.
# Dicionários não possuem um INDEX.

print(dicionario)
print(dicionario["Nome"])

print(dicionario.items())
print(dicionario.keys)
print(dicionario.values)

dicionario["Cor"] = "Vermelho"
print(dicionario)

for chave, valor in dicionario:
    print(f"A chave {chave} tem o valor {valor}")

#-----
# SETS
# Sets são coleções de chaves de dicionários

meu_set = {"Tiago","Jovem","Moreno"}
print(meu_set)
