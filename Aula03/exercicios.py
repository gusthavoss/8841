# 6) Escreva uma função que vai receber o nome e idade do usuário, e dar uma saudacao com o nome dele de acordo com a idade.

def saudacao(nome, idade):
    if idade<12:
        print(f"Oi {nome}, tudo bem?")
    elif idade<18:
        print(f"Opa {nome}, beleza?")
    elif idade<50:
        print(f"Bom dia {nome}, como vai?")
    else:
        print(f"Bom dia senhor {nome}, Como você está?")

# 7) escreva uma função que servirá como uma calculadora simples pra operações de adicão, subtração, multiplicação e divisão, 
# recebendo dois valores do usuario e a operação desejada.

def calc(valor1, valor2, operador):
    if operador == "+":
       print(f"Resultado da soma:{valor1+valor2}")
    elif operador == "-":
       print(f"Resultado da subtração:{valor1-valor2}")
    elif operador == "/":
       print(f"Resultado da divisão:{valor1//valor2}")
    elif operador == "*":
       print(f"Resultado da multiplicação:{valor1*valor2}")
    else:
        print("Não foi possível concluir a operação")
    
# 8) Escreva uma função que receba varios numeros e retorne pro usuário q quantidade de numeros impares acima de um chão escolhido 
# pelo usuario.

def operacao():
    lista_de_numeros = []
    while True:
        resposta = input("Digite um numero? (pra terminar digite x): ")
        if resposta != "x":
            resposta = int(resposta)
            lista_de_numeros.append(resposta)

        if resposta == "x":
            resposta2 = input("Qual o numero minimo(chão) que voce escolhe? ")
            resposta2 = int(resposta2)

            for numero in lista_de_numeros:
                if numero % 2 != 0:
                    if numero > resposta2:
                        print(numero)
        else:
             continue
calc(6,3,"/")
operacao()
