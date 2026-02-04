# Executar função ou conteudo apenas quando o arquivo for executado diretamente:

# import modulos

# print(modulos.soma(4, 5))

# if __name__ == "__main__":
#   saudacao()

#==========================

# Generators

def cria_lista(tamanho):
    lista = []
    for numero in range(0, tamanho):
        lista.append(numero + 1)
    return lista

lista1 = cria_lista(10) # Esse meu objeto "lista1" possui todos os seus valores carregados em memória a todo tempo
for x in lista1:
    print(x)


def criar_generator(tamanho):
    for numero in range(0, tamanho):
        yield numero + 1

generator1 = criar_generator(10) # Esse objeto "generator1" possui apenas o valo mais recente obtido do generator salvo em memória
for x in generator1:
    print(x)

#--------------------------

# Comprehensions

def dobro_lista(x):
    lista = []

    for numero in range(0, x):
        lista.append(numero * 2)

    return lista

print(dobro_lista(10))

lista_comprehension = [x * 2 for x in range(0, 10)]
print(lista_comprehension)

def gera_dict():
    dicionario = {}
    for chave, valor in enumerate(range(100, 200)):
        dicionario["chave"] = valor
    return dicionario

print(gera_dict())

dicionario_comprehension = {chave: valor for chave, valor in enumerate(range(100, 200))}
print(dicionario_comprehension)

# ======================================================================================

# map / reduce / filter

def quadrado(x):
    return x**2

quadrado_1 = lambda x: x**2

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


resultado = map(quadrado_1, lista)
print(list(resultado))

#--------------------------------------------------------------------------------------
from functools import reduce

lista = [5, 10, 15, 20, 25]

def soma(x, y):
    return x + y

soma_1 = lambda x, y: x + y

print(reduce(soma_1, lista))

#-----------------
temperaturas =[25, 30, 35, 36, 12, 21, 41, 22, 23, 36]

sub30 = lambda x: x < 30

print(list(filter(sub30, temperaturas)))

# ========================================
