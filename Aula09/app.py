# JSON

import json

data = {"nome": "Joao", "idade": 30, "Inderesses": ["jogos", "musica"]}

# É possível usar a biblioteca JSON pra converter um dict em str no Python
data_string = json.dumps(data)
print(data_string)

# Também é possivel fazer o oposto, converter uma string (se estiver no formato correto) pra dict
data_string_clean = json.dumps(data, ensure_ascii=False)
print(data_string_clean)

# Podemos escrever e ler o conteudo em arquivos JSON também:
with open("dados.jason", "w", encoding="utf-8") as arquivo:
    json.dump(data, arquivo, ensure_ascii=False)

with open("dados.jason", "r", encoding="utf-8") as arquivo:
    conteudo = json.load(arquivo)

    print(conteudo)

# ====================================================================================================
#Flask -> framework pra APIs

# pip install flask

import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    return "Mensagem da pagina inicial da aplicaçao"

@app.route("/menu")
def menu():
    return "Para coletar informações dos usuarios, acesse /usuarios"

@app.route("/usuarios")
def usuarios():
    return "Nesse momento, ainda não há informações de usuarios disponiveis."


if __name__ == "__main__":
    app.run(debug=True)
