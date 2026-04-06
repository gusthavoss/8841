# Arquivo usado pra armazenar as funções relacionadas ao banco de dados.
import sqlite3
from datetime import datetime


def criar_banco():
    conexao = sqlite3.connect("data/database.db")
    cursor = conexao.cursor()

    cria_tabela_clientes = "CREATE TABLE IF NOT EXISTS clientes (id integer PRIMARY KEY autoincrement, nome, saldo)"
    cria_tabela_auth = "CREATE TABLE IF NOT EXISTS auth (nome, usuario, senha)"

    cursor.execute(cria_tabela_clientes)
    cursor.execute(cria_tabela_auth)

    conexao.commit()
    conexao.close()

def cadastrar(cliente):
    conexao = sqlite3.connect("data/database.db")
    cursor = conexao.cursor()

    registra_cliente_clientes = f"INSERT INTO clientes (nome, saldo) VALUES ('{cliente.nome}', {cliente.saldo})"
    registra_cliente_auth = f"INSERT INTO auth (nome, usuario, senha) VALUES ('{cliente.nome}', '{cliente.usuario}', '{cliente.senha}')"

    cursor.execute(registra_cliente_clientes)
    cursor.execute(registra_cliente_auth)

    conexao.commit()
    conexao.close()

def login(usuario, senha):
    conexao = sqlite3.connect("data/database.db")
    cursor = conexao.cursor()

    checa_auth = f"SELECT nome, senha FROM auth WHERE usuario = '{usuario}'"
    cursor.execute(checa_auth)

    conteudo = cursor.fetchall()
    conexao.close()

    try:
        if senha == conteudo[0][1]:
            return conteudo[0][0]
        else:
            return False
    except IndexError:
        return False

def saldo(nome):
    conexao = sqlite3.connect("data/database.db")
    cursor = conexao.cursor()

    checa_saldo = f"SELECT saldo FROM clientes WHERE nome = '{nome}'"
    cursor.execute(checa_saldo)

    conteudo = cursor.fetchall()
    conexao.close()

    print(f"Saldo disponivel: R${float(conteudo[0][0]):.2f}")

def tranferencia(nome):
    hora_atual = datetime.now().hour

    while True:
        acao = input("Que tipo de transferencia gostaria de efetuar? [deposito/saque]: ")

        if acao in ["deposito", "saque"]:
            valor = input("Qual o valor da transferencia? ")

            if valor.isnumeric() == False:
                print("Valor inválido.")
                continue
            else:
                valor = float(valor)

            if 6 <= hora_atual < 8 or 20 <= hora_atual < 22:
                if valor > 2000:
                    print("Neste horário, só é possivel fazer transferencias de até R$2.000,00")
                    continue

            conexao = sqlite3.connect("data/database.db")
            cursor = conexao.cursor()

            coletar_saldo = f"SELECT saldo FROM clientes WHERE nome = '{nome}'"
            cursor.execute(coletar_saldo)
            saldo_atual = float(cursor.fetchall()[0][0])

            if acao == "deposito":
                novo_saldo = saldo_atual + valor
            else:
                novo_saldo = saldo_atual - valor

            realiza_tranferencia = f"UPDATE clientes SET saldo = '{novo_saldo}' WHERE nome = '{nome}'"
            cursor.execute(realiza_tranferencia)
            conexao.commit()
            conexao.close()

            print(f"Transferência efetuada, novo saldo: R${novo_saldo:.2f}")
            break

        else:
            print("Opção inválida.")
            continue


