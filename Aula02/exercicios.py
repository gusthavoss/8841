import os

# 4) Escreva em script em Python que represente uma quitanda. O seu script deverá apresentar
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

#/opcao = 0
#cesta = ""
#cesta_pos = 0
#fruta = 0
#
#while opcao < 3:
#    opcao = int(input("Menu Principal:\n\n1: Ver cesta\n2: Adicionar uma fruta\n3: Sair\n"))
#
#    if opcao == 1:
#        print(cesta)
    

#    if opcao == 2:
#        fruta = int(input("Menu de frutas:\nDigite a opção que deseja adicionar:\n1 - Banana\n2 - Melancia\n3 - Morango\n"))
#        
#        if fruta == 1:
#           cesta += "Banana, " 
#           print("Banana adicionada com sucesso")
#        elif fruta == 2:
#           cesta += "Melancia, " 
#           print("Melancia adicionada com sucesso")
#        elif fruta == 3:
#           cesta += "Morango, " 
#           print("Morango adicionada com sucesso")
#        else:
#          print("Fruta não encontrada")

# 5) Altere o exercicio 4 para adicionar um preço aos itens comprados, mantendo uma conta com o valor gasto pelo usuário, e no fim, imprima o valor total e os itens na cesta de compras.
# Utilize coleções para mantes o conteudo da cesta de compras.
# Opcional: Mantenha o terminal limpo sempre que possivel.


opcao = 0
cesta = []
cesta_pre = 0
fruta = 0

while opcao < 3:
    opcao = int(input("Menu Principal:\n\n1: Ver cesta\n2: Adicionar uma fruta\n3: Sair\n"))

    if opcao == 1:
        if os.name == "nt":
                os.system("cls")
        else:
                os.system("clear")
        print(cesta)
        print(f"Total: {cesta_pre}")
    

    elif opcao == 2:
        if os.name == "nt":
             os.system("cls")
        else:
                os.system("clear")

        fruta = int(input("Menu de frutas:\nDigite a opção que deseja adicionar:\n1 - Banana\n2 - Melancia\n3 - Morango\n"))
        
        if fruta == 1:
           cesta.insert(len(cesta),"Banana") 
           cesta_pre +=7
           print("Banana adicionada com sucesso")

        elif fruta == 2:
           cesta.insert(len(cesta),"Melancia") 
           cesta_pre +=20
           print("Melancia adicionada com sucesso")
        elif fruta == 3:
           cesta.insert(len(cesta),"Morango") 
           cesta_pre +=5
           print("Morango adicionada com sucesso")
        else:
           print("Fruta não encontrada")