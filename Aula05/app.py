# # Classes -> Tipos de objetos
# # Classes são objetos com estrutura e comportamento definidos.

# # Vamos supor que eu queira criar um novo objeto no Python que represente uma pilha.

class Pilha:

    def __init__(self):
        self.pilha = list()
        self.limite = 5
        self.quantidade = 0

    def empilhar(self, item):
        if self.quantidade < self.limite:
            self.pilha.append(item)
            self.quantidade += 1
            return(f"Objeto empilhado com sucesso!")
        else:
            return(f"Essa pilha já está no limite de {self.limite} objetos empilhados!")
        
    def desempilhar(self):
        if self.quantidade > 0:
            self.pilha.pop(-1)
            self.quantidade -= 1
            return(f"Item removido do topo da pilha com sucesso!")
        else:
            return("Essa pilha já está vazia!")

pilha_de_pratos = Pilha()
pilha_de_brinquedos = Pilha()
pilha_de_roupas = Pilha()

lista = list()

print(pilha_de_roupas.pilha)
print(pilha_de_roupas.empilhar("Camisa vermelha"))
print(pilha_de_roupas.pilha)
print(pilha_de_roupas.empilhar("Camisa verde"))
print(pilha_de_roupas.empilhar("Camisa amarela"))
print(pilha_de_roupas.empilhar("Calça curta"))
print(pilha_de_roupas.empilhar("Calça azul"))
print(pilha_de_roupas.empilhar("Camisola"))
print(pilha_de_roupas.pilha)
print(pilha_de_roupas.desempilhar())
print(pilha_de_roupas.desempilhar())
print(pilha_de_roupas.desempilhar())
print(pilha_de_roupas.desempilhar())
print(pilha_de_roupas.desempilhar())
print(pilha_de_roupas.desempilhar())

# # HERANÇA em Classes

class Funcionario:

    def __init__(self):
        self.salario = 0
        self.nome = ""

    def definir_nome(self, nome):
        self.nome = nome

    def definir_salario(self, salario):
        self.salario = salario

class Gerente(Funcionario):

    def __init__(self):
        self.bonus = 1.3

    def aplica_bonus(self):
        self.salario = self.salario * self.bonus

joao = Funcionario()
joao.definir_nome("João")
joao.definir_salario(5000.00)
print(joao.salario)

pedro = Gerente()
pedro.definir_nome("Pedro")
pedro.definir_salario(5000.00)
pedro.aplica_bonus()
print(pedro.salario)

# POLIMORFISMO em Classes

class Funcionario2:

    def __init__(self):
        self.salario = 3000
        self.nome = ""

    def definir_nome(self, nome):
        self.nome = nome

class Gerente2(Funcionario2):

    def __init__(self):
        self.salario = 4500

tiago = Funcionario2()
print(tiago.salario)

caio = Gerente2()
print(caio.salario)
