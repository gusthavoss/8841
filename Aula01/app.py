# PRINT é um comando utilizado para exibir mensagens na tela

print("Olá Mundo!")
print("Meu nome é gusthavo")

# INPUT é o comando utilizado pra coletar informações via terminal

input("Qual o seu nome? ")

# CTRL + S + Salvar as alterações
# CTRL + L = Limpar o terminal

#VARIÁVEIS são palavras que armazenam um valor

nome = "Gusthavo Souza"
print("É um prazer tê-lo aqui, ",nome)
print("É um prazer tê-lo aqui, {}".format(nome))
print(f"É um prazer tê-lo aqui, {nome}")








nome = "Husthavo Silva" #String







numero01 =10
numero02 = 5

numero03 = numero01 + numero02
print(numero03)

#========================================

nome01 = "Gusthavo"
nome02 = 10

nome03 = nome01 * nome02

#========================================

palavra = "500"
numero = int(palavra)
print(numero)

#========================================
# Métodos disponiveis pra STR
nome_completo = "Gusthavo Souza e Silva"

nome_completo01 = come_completo.lower()
print(nome_completo01)

nome_completo03 = nome_completo.replace("i","h")
print(nome_completo03)

nome_completo04 = nome_completo.isnumeric()
print(nome_completo04)





# ====================================== 
# Estruturas de decisão

idaide = 29
if idade > 18:
    print("Você é maior de idaide.>")
    print("Você já pode dirigir!")

elif idade > 15:
    print("Você não é maior de idade, mas já é um adolecente")

elif idade > 10:
    print("Você é novo de mais")

else:
    print("Você é novo de mais")

print("Esta linha sempre vai ser executada, e não depende do resultado do 'if'")

# ====================================== 
#Estrutura de repetição
