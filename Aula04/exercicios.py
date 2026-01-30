# 9) Assumindo que uma lata de tinta pinte 3m² de uma superficie,. ecreva um programa que possua uma função que receba as dimenções 
# de uma parede, e calcule quantas latas de tinta o usuario precisará comprar pra pintar aquela parede.

#from math import ceil

#def area(x, y):
#    area_total = x * y
#    latas = area_total / 3
#    latas = ceil(latas)

#    print(f"Pra pintar essa parede, voce vai precisar de {latas} latas.")

#altura = float(input("Qual a altura da parede? "))
#comprimento = float(input("Qual o comprimento da parede? "))

#area(altura, comprimento)

# 10) Crie um programa que receba um numero de jogadores entre 2 e 20 pra participarem de um sorteio, e os escolha da seguinte lista:

# lista = ["Joao", "Maria", "Tiago", "Amanda", "Emanuele", "Caio", "Suzana", "Miguel", 
# "Rosangela", "Rian", "Lucimar", "Ulisses", "Leonardo", "Kaique", "Bruno", "Raquel", 
# "Benedito", "Tereza", "Valmir", "Joaquim"]

# OBS: O programa não poderá pegar nomes repetidos.

# Em seguida, o programa deverá perguntar quantos ganhadores deverão ter nesse sorteio.

# OBS: A mesma pessoa não pode ganhar duas vezes.
# OBS2: O numero de vencedores não pode ser maior do que o numero de participantes.

# Mostre na tela quais foram os ganhadores do sorteio.
import random

lista = ["Joao", "Maria", "Tiago", "Amanda", "Emanuele", "Caio", "Suzana", "Miguel", "Rosangela", "Rian", "Lucimar", "Ulisses", "Leonardo", "Kaique", "Bruno", "Raquel", "Benedito", "Tereza", "Valmir", "Joaquim"]

numero_de_jogadores = int(input("Quantos jogadores vão participar desse sorteio? "))

lista_de_participantes = []
for numero in range(0, numero_de_jogadores):
    pessoa_escolhida = random.choice(lista)
    lista_de_participantes.append(pessoa_escolhida)
    lista.remove(pessoa_escolhida)

numero_de_ganhadores = int(input("Quantos vencedores haverão nesse sorteio? "))

if numero_de_ganhadores > numero_de_jogadores:
    print("O numero de venedores não pode ser aior do que o numero de participantes.")

else:
    ganhadores = []
    for numero in range(0, numero_de_ganhadores):
        ganhador = random.choice(lista_de_participantes)
        ganhadores.append(ganhador)
        lista_de_participantes.remove(ganhador)

    print(f"Os ganhadores do sorteio foram: {ganhadores}")


# 11) Escreva um programa que conte as vogais da letra da musica faroeste caboclo.
# Dica1 - 2587 vogais
# Dica2 - encode / decode

arquivo = open("faroeste_caboclo.txt", "r")
conteudo = arquivo.readlines()
contagem_vog = 0

def vogais(letra):
    vogais = "aeiouAEIOUãõÃÕáéíóúÁÉÍÓÚàèìòùÀÈÌÒÙâêîôûÂÊÎÔÛäëïöüÄËÏÖÜ"
    if letra in vogais:
        return True
    else:
        return False

for linha in conteudo:
    palavra = linha
    for letra in palavra:
        
        if vogais(letra):
            contagem_vog += 1
print(contagem_vog)


# 12) Escreva um programa que realize um cadastro, esse programa deverá coletar do usuario informações de:
# nome, cpf, idade e sexo.
#Depois de coletar essas informações, elas deverão ser salvas em um arquivo CSV.
# Voces precisarão pesquisar como salvar linhas em um arquivo csv no python.

# 13) Escreva um programa em Python que simule uma dança das cadeiras, esse programa utilizará o modulo "random" e suas funções 
# "choice" ou "randint". O jogo deverá iniciar com 9 cadeiras e 10 participantes, a cada rodada um partipante será removido e uma 
# cadeira também. A pessoa a ser eliminada deverá ser escolhida de forma aleatória.

# Opcional: Utilize a biblioteca time pra adicionar um delay entre as rodadas.
# Opcional: Tente remover uma pessoa aleatória por rodada sem usar a função choice.

# import random

# lista = [1, 2, 3]

# escolhido = random.choice(lista) # Escolhe um valor aleatório de uma lista
# escolhido = random.randint(0, 100) # Escolhe um numero inteiro aleatório

# 1 - Importar o modulo random
# 2 - Criar lista de participantes
# 3 - Criar um loop pras rodadas
# 4 - Buscar uma maneira de escolher um participante aleatório e removê-lo
# 5 - Sair do loop quando só sobra uma pessoa na lista
