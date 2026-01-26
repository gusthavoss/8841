# 1) Em muitos programas, nos é solicitado preenchimento de algumas informações como nome, 
# idade e CPF para cadastro. Escreva um script simples em Python que solicite essas 
# informações cadastrais do usuário e em seguida as apresente da seguinte forma:

# ------------------------------
# Confirmação de cadastro:
# Nome: Tiago P. Lima
# CPF: 132.465.789-45
# Idade: 29
# ------------------------------

nome = input("Nome: ")
idade = input("Idade: ")
cpf = input("CPF: ")

print(f" ------------------------------\nConfirmação de cadastro:\n Nome: {nome}\n CPF: {cpf}\n Idade: {idade}\n ------------------------------")



# 2) Escreva um script em Python que receba dois numeros e que realize as seguintes operações com eles:
# - Soma dos dois numeros
# - Diferença dos dois numeros
# Os resultados deverão ser apresentados no formato:
# 4 + 2 = 6
# 4 - 2 = 2

num1 = float(input("Numero 1: "))
num2 = float(input("Numero 2: "))

num3 = num1 + num2
num4 = num1 - num2
print(f"{num1} + {num2} = {num3}\n{num1} + {num2} = {num4}")

# 3) Escreva um script em Python que traduza a seguinte frase em uma frase legível, removendo os "x" dela:
# Umxpratoxdextrigoxparaxtrêsxtigresxtristes

frase = "Umxpratoxdextrigoxparaxtrêsxtigresxtristes"
frasetradusida = frase.replace("x"," ")

# 4) Escreva um script em Python que receba o ano de nascimento do usuário, e que retorne à qual geração esse usuário pertence, se baseando na idade. Utilize a tabela a seguir pra calcular:

# Geração    Intervalo
# Boomer     Antes de 1964
# Geração X  1965 - 1979
# Geração Y  1980 - 1994
# Geraçãp Z  1995 - Atual

ano = int(input("Que ano você nasceu: "))
if ano<1965:
    print("Boomer")
elif ano<1979:
    print("Geração X")
elif ano<1994:
    print("Geração Y")
else:
    print("Geração Z")

