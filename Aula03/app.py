# Funções
# Trechos de código que podem ser re-utilizados diversas vezes durante a extenção do seu script sem a necessidade de repetir todo o código.

import os

def limpa_tela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

limpa_tela()

# Criar uma função que recebe um parâmetro:

def saudacao(nome):
    print(f"Prazer em conhecê-lo, {nome}!")

saudacao("Tiago")
saudacao("Caio")
saudacao("Kaique")

pessoa = input("Qual é o seu nome? ")
saudacao(pessoa)

# Criar funções com multiplos parâmetros:

def soma(x, y):
    resultado = x + y
    print(f"O resultado de {x} + {y} é {resultado}")

# soma(4,23)
# soma(7,11)
# soma(5,0)

# Criar uma função com um retorno

def par(numero):
    if numero % 2 ==0:
        resultado = True
    else:
        resultado = False
    
    return resultado


x = par(45)
print(x)

print(par(12))



# Alterando  o funcionamento padrão dos parâmetros de uma função:

def subtracao(a, b=2):
    print(a - b)

subtracao(b=10,a=6)

# Permite o uso da função apenas com argumentos não posicionais (1st, 2nd, 3rd)
def soma(*, c ,d):
    print(c + d)

soma(4, 8)

# Permite o uso da função apenas com argumentos posicionais (1st, 2nd, 3rd)
def soma( c ,d ,/):
    print(c + d)

soma(4, 8)

# Criando uma função com um nomero x de parametros:
def soma(*args):
     resultado = 0
     for numero in args:
         resultado += numero
     print(resultado)

soma(12,2,0,5,6)
soma(44, 5)
soma()

def idade(**kargs):
    for pessoa, idade in kwargs.items():
        print(f"A pessoa '{pessoa}' tem {idade} anos.")

idade(Tiago=29, João=35, Carol=22)

# Funções anônimas / Funções Lambda

def soma(x, y):
    return x + y

print(soma(12, 5))

soma_lambda = lambda x, y: x + y
print(soma_lambda(12, 5))

# Maneiras diferentes de delimitar strings no Python:
print('''Testando o "nome" gota d'agua nessa linha''')
print("""Testando o "nome" gota d'agua nessa linha""")
print('Testando o "nome" gota nessa linha')
print("Testando o gota d'agua nessa linha")
