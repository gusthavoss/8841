import sqlite3, random, time

conexao = sqlite3.connect("estoque.db")
cursor = conexao.cursor()

# Criar as tabelas
tabela_comida = """
CREATE TABLE IF NOT EXISTS comidas (
id integer primary key autoincrement, 
nome, 
preco, 
quantidade
)"""

tabela_bebidas = """
CREATE TABLE IF NOT EXISTS bebidas (
id integer primary key autoincrement, 
nome, 
preco, 
quantidade
)"""

cursor.execute(tabela_comida)
cursor.execute(tabela_bebidas)
conexao.commit()

# Preencher as tabelas
comidas = [("Hamburger", 25.00, 5), ("Hotdog", 12.00, 5), ("Chocolate", 5.00, 5), ("Pão", 1.50, 5), ("Misto Quente", 4.00, 5)]
bebidas = [("Coca Cola", 10.00, 7), ("Fanta", 8.00, 7), ("Café", 2.50, 7)]

for comida in comidas:
    registra_comida = f'INSERT INTO comidas (nome, preco, quantidade) VALUES ("{comida[0]}", "{comida[1]}", "{comida[2]}")'
    cursor.execute(registra_comida)

for bebida in bebidas:
    registra_bebida = f'INSERT INTO bebidas (nome, preco, quantidade) VALUES ("{bebida[0]}", "{bebida[1]}", "{bebida[2]}")'
    cursor.execute(registra_bebida)

conexao.commit()

# Criar uma função do cliente que vai fazer o pedido

def cliente():
    # Coleta o nome de todas as comidas e bebidas disponiveis:
    coleta_comidas = "SELECT nome FROM comidas"
    cursor.execute(coleta_comidas)
    lista_comidas = cursor.fetchall()

    coleta_bebidas = "SELECT nome FROM bebidas"
    cursor.execute(coleta_bebidas)
    lista_bebidas = cursor.fetchall()

    # Seleciona aleatóriamente uma comida e uma bebida pra adicionar no pedido:
    pedido = {}
    pedido["comida"] = random.choice(lista_comidas)[0]
    pedido["bebida"] = random.choice(lista_bebidas)[0]

    # Checa a quantidade disponivel da comida e bebida escolhidos:
    quantidade_atual_comida = f'''SELECT quantidade FROM comidas WHERE nome = "{pedido['comida']}"'''
    quantidade_atual_bebida = f'''SELECT quantidade FROM bebidas WHERE nome = "{pedido['bebida']}"'''

    cursor.execute(quantidade_atual_comida)
    qnt_comida = int(cursor.fetchall()[0][0])

    cursor.execute(quantidade_atual_bebida)
    qnt_bebida = int(cursor.fetchall()[0][0])

    if qnt_comida == 0:
        print(f"A comida selecionada, {pedido["comida"]}, está fora de estoque.")

    elif qnt_bebida == 0:
        print(f"A bebida selecionada, {pedido["bebida"]}, está fora de estoque.")

    else:
        atualiza_comida = f'''UPDATE comidas SET quantidade = {qnt_comida - 1} WHERE nome = "{pedido['comida']}"'''
        atualiza_bebida = f'''UPDATE bebidas SET quantidade = {qnt_bebida - 1} WHERE nome = "{pedido['bebida']}"'''

        cursor.execute(atualiza_comida)
        cursor.execute(atualiza_bebida)
        conexao.commit()
    
        # Checa o preço dos itens escolhidos e finaliza a venda:

        preco_comida = f'''SELECT preco FROM comidas WHERE nome = "{pedido['comida']}"'''
        preco_bebida = f'''SELECT preco FROM bebidas WHERE nome = "{pedido['bebida']}"'''

        cursor.execute(preco_comida)
        prc_comida = float(cursor.fetchall()[0][0])

        cursor.execute(preco_bebida)
        prc_bebida = float(cursor.fetchall()[0][0])

        preco_total = prc_comida + prc_bebida

        print(f"Pedido feito! {pedido["comida"]} + {pedido['bebida']}! Preço: R${preco_total:.2f}")

for pessoa in range(0, 30):
    cliente()
    time.sleep(1)
