# Arquivo principal do programa, contém o menu inicial.
from os import system, name
from datetime import datetime
from lib.classes import Cliente
from lib.database_services import saldo, tranferencia, criar_banco, cadastrar, login

def clear_terminal():
    system("cls" if name == "nt" else "clear")

def menu_principal(nome):
    while True:
        acao = input("""===============================
Que ação gostaria de efetuar?
1 - Checar o saldo
2 - Realizar uma transferencia
3 - Sair\n""")
        
        if acao == "1":
            clear_terminal()
            saldo(nome)
        
        elif acao == "2":
            hora_atual = datetime.now().hour
            if 0 <= hora_atual < 6 or 22 <= hora_atual < 24:
                print("O caixa eletrônico não permite transferencias nesse horário.")
                continue
            clear_terminal()
            tranferencia(nome)

        elif acao == "3":
            clear_terminal()
            print("Fazendo logout...")
            break

        else:
            clear_terminal()
            print("Opção inválida.")

def menu_login():
    criar_banco()

    while True:
        escolha = input("""
Bem vindo ao caixa eletrônico:
                        
1 - Se registrar no banco.
2 - Se logar no sistema.\n""")
        
        if escolha == "1":
            clear_terminal()
            nome = input("Qual o seu nome? ")
            usuario = input("Escolha um nome de usuário para login: ")
            senha = input("Escolha sua senha: ")
            cliente = Cliente(nome=nome, usuario=usuario, senha=senha)
            cadastrar(cliente=cliente)
            clear_terminal()
            print("Conta registrada no sistema.")
            
        elif escolha == "2":
            clear_terminal()
            usuario = input("Digite seu usuário: ")
            senha = input("Digite sua senha: ")
            clear_terminal()
            
            validacao = login(usuario=usuario, senha=senha)
            if validacao == False:
                print("Usuário ou senha inválidos!")
            else:
                clear_terminal()
                menu_principal(validacao)

if __name__ == "__main__":
    menu_login()

