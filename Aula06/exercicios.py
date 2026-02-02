# 16) Crie um script que simule uma lanchonete

# - Essa lanchonete deverá ter 5 tipos de comida e 3 tipos de bebida no cardápio. Essas informações deverão ser salvas em um banco de dados, em tabelas diferentes.
# - Quando clientes chegarem na lanchonete, eles farão um pedido aleatório de 1 comida + 1 bebida.
# - A lanchonete deverá ter um numero limitado de porções dessas comidas/bebidas. comida = 5, bebidas = 7.
# - Quando um cliente fizer um pedido, ele deverá ser notificado se as opções escolhidas estão disponiveis e quais seus preços.
# - Mantenha as tabelas do banco de dados atualizados sempre que uma nova venda for feita.
# - No fim, simule 30 clientes chegando um após o outro na lanchonete.

import sqlite3

conexao = sqlite3.connect("empresa.db") 
cursor = conexao.cursor()               

comando_cria_tabela_comida = """
CREATE TABLE IF NOT EXISTS comida (
id integer primary key autoincrement, 
nome text, 
preco float,
quantidade integer
)"""


comando_cria_tabela_bebida = """
CREATE TABLE IF NOT EXISTS bebida (
id integer primary key autoincrement, 
nome text, 
preco float,
quantidade integer
)"""

cursor.execute(comando_cria_tabela_comida)
cursor.execute(comando_cria_tabela_bebida)

conexao.commit()


comando_adiciona_comida1 = """
INSERT INTO comida (nome, preco, quantidade)
VALUES ("Batata Frita", 9.50, 20)
"""

comando_adiciona_comida2 = """
INSERT INTO comida (nome, preco, quantidade)
VALUES ("Hamburger", 20.70, 30)
"""

comando_adiciona_comida3 = """
INSERT INTO comida (nome, preco, quantidade)
VALUES ("Pizza", 37.40, 40)
"""

comando_adiciona_comida4 = """
INSERT INTO comida (nome, preco, quantidade)
VALUES ("Esfiha", 7.30, 10)
"""

comando_adiciona_comida5 = """
INSERT INTO comida (nome, preco, quantidade)
VALUES ("Pastel", 12.10,25)
"""

cursor.execute(comando_adiciona_comida1)
cursor.execute(comando_adiciona_comida2)
cursor.execute(comando_adiciona_comida3)
cursor.execute(comando_adiciona_comida4)
cursor.execute(comando_adiciona_comida5)

conexao.commit()

comando_adiciona_bebida1 = """
INSERT INTO bebida (nome, preco, quantidade)
VALUES ("Suco", 5.50, 20)
"""

comando_adiciona_bebida2 = """
INSERT INTO bebida (nome, preco, quantidade)
VALUES ("Refrigerante", 8.70, 10)
"""

comando_adiciona_bebida3 = """
INSERT INTO bebida (nome, preco, quantidade)
VALUES ("agua", 3.40, 30)
"""

cursor.execute(comando_adiciona_bebida1)
cursor.execute(comando_adiciona_bebida2)
cursor.execute(comando_adiciona_bebida3)

conexao.commit()

# menu cliente ============================================|
pedido = ()
opcao = 0

while opcao != 4:
    while opcao != 3:
        print(f"""Menu
            {pedido}
            O que deseja pedir:
            1 - Comida
            2 - Bebida
            3 - Fechar pedido
            4 - Encerrar programa""")
        opcao = int(input(" : "))
        if opcao == 1:
            comando_checa_tabela = "SELECT * FROM comida"
            print(cursor.execute(comando_checa_tabela))
            
            comida = int(input("O que vai querer: "))
            comando_checa_tabela = f"SELECT quantidade FROM bebida WHERE id = {comida}"
            if cursor.execute(comando_checa_tabela) == 0:
                print("item indisponível")
            else:  
                comando_checa_tabela = f"SELECT * FROM bebida WHERE id = {comida}"
                pedido.append(cursor.execute(comando_checa_tabela))
                comando_atualiza_tabela = f'UPDATE bebida SET quantidade = quantidade-1 WHERE id = {comida}'
                cursor.execute(comando_atualiza_tabela)
                conexao.commit()
        
        elif opcao == 2:
            comando_checa_tabela = "SELECT * FROM bebida"
            print(cursor.execute(comando_checa_tabela))
            
            bebida = int(input("O que vai querer: "))
            comando_checa_tabela = f"SELECT quantidade FROM bebida WHERE id = {bebida}"
            if cursor.execute(comando_checa_tabela) == 0:
                print("item indisponível")
            else:  
                comando_checa_tabela = f"SELECT * FROM bebida WHERE id = {bebida}"
                pedido.append(cursor.execute(comando_checa_tabela))
                comando_atualiza_tabela = f'UPDATE bebida SET quantidade = quantidade-1 WHERE id = {bebida}'
                cursor.execute(comando_atualiza_tabela)
                conexao.commit()
        
        elif opcao == 3:
            print("Pedido fechado")
            print(pedido)
        
        elif opcao == 4:
            print("Encerrando...")
        
        else:
            print("Opção incorreta, tente novamente")
    
    print("Próximo cliente")



conexao.commit()



comando_checa_tabela = "SELECT * FROM comida"
comando_checa_tabela2 = "SELECT * FROM bebida"
cursor.execute(comando_checa_tabela)
cursor.execute(comando_checa_tabela2)

