# 17) Assuma que há uma empresa com varios sensores de temperatura espalhados por seu predio, que geram leituras constantes. O 
# sistema dessa empresa precisa processar essas leituras, filtrá-las e gerar um relatório.

# - Simular os sensores (Criar generators para a geração das leituras de temperatura em celcius.)
# - Filtrar as leituras inválidas (filter) (menor que -20°c e maior que 50°c)
# - Converter esses valores (map) pra um formato de fahrenheit
# - Gerar um relatório (reduce) pra:
#   - Temperatura media
#   - Temperatura maxima
# - Faça com que esse script não seja executado automaticamente em caso de importação.

# - Minha Tentativa -
import random

temperatura = []

def gerar_temperatura(quantidade):
    
    for i in int(quantidade):
        temperatura[i]

gerar_temperatura(10)
print(temperatura)
# -----------------------------------

from random import randint
from functools import reduce

# Generator:
def sensor_temperatura():
    for exec in range(0, 100):
        temperatura = randint(-30, 60)
        yield temperatura

def filtra_temperaturas(temperatura):
    if temperatura < -20 or temperatura > 50:
        return False
    else:
        return True
    
def celcius_pra_fahrenheit(temperatura):
    fahrenheit = temperatura * 9/5 + 32
    return fahrenheit

def main():
    temperaturas = sensor_temperatura()

    leituras_validas = filter(filtra_temperaturas, temperaturas)

    leituras_fahrenheit = map(celcius_pra_fahrenheit, leituras_validas)

    list_leituras_fahrenheit = list(leituras_fahrenheit)
    soma = reduce(lambda x, y: x + y, list_leituras_fahrenheit)

    media = soma / len(list_leituras_fahrenheit)
    maxima = max(list_leituras_fahrenheit)

    print(f"Temperatura média: {media:.1f}°f, temperatura máxima: {maxima:.1f}°f.")

if __name__ == "__main__":
    main()

# 18) Escreva um programa utilizando funções que realize um cadastro.
# Deverão ser coletadas as seguintes informações:

# CPF
# Nome
# Idade
# Sexo
# Cidade

# Os registros deverão ser armazenados em um arquivo CSV
# Para manter o padrão brasileiro, o CSV deverá utilizar o ";" como delimitador
# O programa deverá possuir uma função de colsulta (por nome ou cpf)
# O programa deverá possuir uma função de exclusão (por cpf)
# O programa deverá ter tratamento de erros, com a finalidade de que o programa nunca dê uma exceção, e também de que ele não aceite dados incorretos/inválidos.

import os, csv

def menu():
    print("=============================================")
    print("Bem vindo ao sistema de gerencia de usuarios.")
    while True:
        opcao = input("""
O que deseja fazer?
1 - Consultar um valor no banco.
2 - Cadastrar um valor no banco.
3 - Remover um valor do banco.
4 - Fechar o programa.\n\n""")
        
        os.system("cls" if os.name == "nt" else "clear")

        if opcao == "4":
            print("Obrigado por utilizar o sistema de gerencia de usuarios. Fechando o programa...")
            break

        elif opcao == "3":
            exclusao()

        elif opcao == "2":
            cadastro()

        elif opcao == "1":
            consulta()

        else:
            print("Voce digitou um valor inválido.\n\n")

def cadastro():
    while True:
        # Coletamos um CPF válido pra registrar:
        while True:
            cpf = input("Qual o CPF da pessoa que deseja adicionar? ")
            if validacao("CPF", cpf) == False:
                print("CPF inválido, digite novamente.")
                continue
            break

        # Coletamos o nome pra registrar:
        nome = input("Qual o nome da pessoa que deseja adicionar? ")

        # Coletamos uma idade válida pra registrar:
        while True:
            idade = input("Qual a idade da pessoa que deseja adicionar? ")
            if validacao("IDADE", idade) == False:
                print("Idade inválida, digite novamente.")
                continue
            break

        # Coletamos o sexo pra registrar:
        sexo = input("Qual o sexo da pessoa que deseja adicionar? ")
        # Coletamos a cidade de origem pra registrar:
        cidade = input("Qual a cidade de origem da pessoa que deseja adicionar? ")

        dados_a_cadastrar = [cpf, nome, idade, sexo, cidade]

        with open("banco.csv", "a", newline="") as arquivo:
            writer = csv.writer(arquivo, delimiter=";")
            writer.writerow(dados_a_cadastrar)

        print("Cadastro efetuado com sucesso!")

        # Criamos uma variavel de controle pra saber se vamos parar o loop de cadastro ou não:
        resposta = True

        # Iniciamos um loop pra questionar o usuário se vamos parar o loop de cadastro ou não:
        while True:
            cadastrar_novo = input("Gostaria de cadastrar outro usuário? [S/N]: ")

            # Se o usuário escolher parar o loop de cadastro, registramos isso na variavel de controle e paramos o loop de questionamento.
            if cadastrar_novo.lower() == "n":
                resposta = False
                break

            # Se o usuário escolher continuar o loop de cadastro, apenas paramos o loop de questionamento.
            elif cadastrar_novo.lower() == "s":
                break

            # Se o usuário digitar um valor inválido, perguntamos novamente.
            else:
                print("Resposta inválida.")

        # Se no loop de questionamento, o usuário escolheu parar o loop de cadastro, como registrado na variavel de controle, paramos o loop.
        if resposta == False:
            os.system("cls" if os.name == "nt" else "clear")
            break

def validacao(tipo, dado):
    if tipo == "CPF":
        cpf_limpo = dado.replace(".", "").replace("-", "").strip()
        if len(cpf_limpo) == 11 and cpf_limpo.isnumeric() == True:
            return True
        else:
            return False

    elif tipo == "IDADE":
        idade_limpa = dado.strip()
        if idade_limpa.isnumeric() == True and 0 <= int(idade_limpa) < 130:
            return True
        else:
            return False

def consulta():
    while True:
        resposta = input("""Que tipo de consulta gostaria de fazer?
0 - Consulta por CPF
1 - Consulta por NOME\n\n""")
        
        os.system("cls" if os.name == "nt" else "clear")
        if resposta in "01" and len(resposta) == 1:
            break
        else:
            print("Opção inválida, escolha novamente.")

    while True:
        if resposta == "0":
            valor = input("Digite o CPF que quer consultar: ")
            if validacao("CPF", valor) == False:
                print("CPF inválido.")
                continue
        elif resposta == "1":
            valor = input("Digite o nome que quer consultar: ")

        break

    os.system("cls" if os.name == "nt" else "clear")

    with open("banco.csv", "r") as arquivo:
        conteudo = csv.reader(arquivo, delimiter=";")

        valor_encontrado = False

        for linha in conteudo:
            if linha[int(resposta)].lower() == valor.lower():
                valor_encontrado = True
                print(f"""Valor encontrado:
CPF: {linha[0]}
Nome: {linha[1]}
Idade: {linha[2]}
Sexo: {linha[3]}
Cidade: {linha[4]}""")
                break

        if valor_encontrado == False:
            print("Valor não encontrado.")

def exclusao():
    while True:
        cpf = input("Digite o CPF da pessoa que deseja remover do banco: ")
        if validacao("CPF", cpf) == True:
            break
        else:
            print("CPF inválido.")

    with open("banco.csv", "r") as arquivo_inicial, open("banco_editado.csv", "a", newline="") as arquivo_editado:
        reader = csv.reader(arquivo_inicial, delimiter=";")
        writer = csv.writer(arquivo_editado, delimiter=";")

        pessoa_removida = False
        for linha in reader:
            if linha[0] != cpf:
                writer.writerow(linha)
            else:
                print("Pessoa removida do banco.")
                pessoa_removida = True

        if pessoa_removida == False:
            print("Nenhuma pessoa com esse CPF encontrada no banco.")

    os.remove("banco.csv")
    os.rename("banco_editado.csv", "banco.csv")


if __name__ == "__main__":
    menu()
