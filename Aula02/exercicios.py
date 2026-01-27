# 1) Escreva em script em Python que represente uma quitanda. O seu script deverá apresentar
# opções de frutas, e cada vez que voce escolher a fruta desejada, a fruta deverá ser
# adicionada a uma cesta de compras.

# Menu Principal:
#
# 1: Ver cesta
# 2: Adicionar uma fruta
# 3: Sair
#
# Menu de frutas:
# Digite a opção que deseja adicionar:
# 1 - Banana
# 2 - Melancia
# 3 - Morango
#
# Melancia adicionada com sucesso!
#
# O menu de frutas deverá retornar para o menu principal depois que o usuário escolher uma
# fruta pra adicionar na cesta. Caso a pessoa digite um numero/opção que não existe, o 
# notifique. O programa só deverá finalizar caso a pessoa digite o numero 3 no menu 
# principal.

opcao = 0
cesta = ""
cesta_pos = 0
fruta = 0

while opcao < 3:
    opcao = int(input("Menu Principal:\n\n1: Ver cesta\n2: Adicionar uma fruta\n3: Sair\n"))

    if opcao == 1:
        print(cesta)
    

    if opcao == 2:
        fruta = int(input("Menu de frutas:\nDigite a opção que deseja adicionar:\n1 - Banana\n2 - Melancia\n3 - Morango\n"))
        
        if fruta == 1:
           cesta = cesta + "Banana, " 
           print("Banana adicionada com sucesso")
        elif fruta == 2:
           cesta += "Melancia, " 
           print("Melancia adicionada com sucesso")
        elif fruta == 3:
           cesta = "Morango, " 
           print("Morango adicionada com sucesso")
        else:
           print("Fruta não encontrada")
    