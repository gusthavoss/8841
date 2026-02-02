# Banco de dados

import sqlite3
# Este modelo de banco de dados salva suas informações em um formato de tabelas.

conexao = sqlite.connect("empresa.db") # Criar uma conexao com o banco de dados.
cursor = conexao.cursor()               # Utilizado pra editar o banco.

# Criar uma tabela no banco de dados:
comando_cria_tabela = """
CREATE TABLE IF NOT EXISTS funcionarios (
id integer primary key autoincrement, 
nome text, 
idade integer
)"""

cursor.execute(comando_cria_tabela)
# Até esse momento, temos um banco de dados com uma unica tabela, e essa tabela está vazia.

# Criar um comando pra adicionar valores em uma tabela no banco de dados:
comando_adiciona_funcionario1 = """
INSERT INTO funcionarios (nome, idade)
VALUES ("Tiago", 29)
"""

comando_adiciona_funcionario2 = """"
INSERT INTO funcionario (nome, idade)
VALUES ("Caio", 28)
"""

comando_adiciona_funcionario3 = """"
INSERT INTO funcionario (nome, idade)
VALUES ("kaique", 32)
"""

cursor.execute(comando_adiciona_funcionario1)
cursor.execute(comando_adiciona_funcionario2)
cursor.execute(comando_adiciona_funcionario3)
conexao.commit() # Salvar as alterações feitas até então no banco.

# Criar um comando pra remover valores de uma tabela de banco de dados:
comando_remove_item = 'DELETE FROM funcionarios WHERE nome = "Tiago"'
cursor.execute(comando_remove_item)
conexao.commit()

# Criar um comando pra editar valores em uma tabela do banco de dados:
comando_atualiza_tabela = 'UPDATE funcionarios SET idade = 34 WHERE id = 3'
cursor.execute(comando_atualiza_tabela)
conexao.commit()


# Criar um comando para coletar as informações de dentro da tabela no banco de dados:
comando_checa_tabela = "SELECT * FROM funcionarios"# Colete todas as informações da tabela funcionarios
comando_checa_tabela2 = "SELECT idade FROM funcionarios" # Colete todas as informações da coluna idade da tabela funcionarios
comando_checa_tabela3 = 'SELECT * FROM funcionarios WHERE nome = "Caio"'

cursor.execute(comando_checa_tabela)
conteudo = cursor.fetchall()
for linha in conteudo:
    print(linha)

# =====================================================================================
# Tratamento de erros Python

try:
    nome = int("Tiago")     # Tenta executar oo código

except ValueError as error:     # Caso o TRY dê a exceção X
    (f"Erro ao rodar comando: {error}")

except ZeroDivisionError as error:
    print(f"Erro ao rodar comando: {error}")

except Exception as error:
    print(f"Erro não previsto: {error}")

else:   # Se não ocorrer nenhum erro
    print("Comando rodado sem erros")

finally:    # Sempre é executado:
    print("Trecho de código sempre executado")