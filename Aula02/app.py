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

# FOR (para) ===================
numero = 0
for numero in range(0, 71):
    print(f"Valor atual da variavel do for: {numero}")

nome = "Tiago"

for letra in nome:
    print(letra)
