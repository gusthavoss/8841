# 14) Crie uma classe que represente um ônibus. O onibus deverá conter os seguintes atributos:

# capacidade total
# n_passageiros
# movimento (s/n)

# Os objetos da classe Onibus precisarao ter os seguintes comportamentos:

# embarcar
# desembarcar
# começar_a_se_mover
# parar_de_se_mover

# A capacidade total deverá ser de 45 pessoas. Não será possivel embarcar pessoas além desse limite. Sempre embarcar o maximo possivel de pessoas que puder acomodar.
# Se o onibus estiver vazio, não será possivel desembarcar passageiros.
# Pessoas não podem embarcar ou desembarcar se o onibus estiver em movimento.

class Onibus:

    def __init__(self):
        self.capacidade_total = 45
        self.passageiros = 0
        self.movimento = False

    def embarcar(self, novos_passageiros):
        if self.movimento == True:
            return(f"Não é possivel embarcar passageiros no momento pois o ônibus está em movimento!")
        
        elif self.passageiros == self.capacidade_total:
            return(f"Não é possivel embarcar passageiros no momento pois o ônibus está lotado!")
        
        elif self.passageiros + novos_passageiros > self.capacidade_total:
            total_pessoas = self.passageiros + novos_passageiros
            passageiros_de_fora = total_pessoas - self.capacidade_total
            conseguiram_entrar = novos_passageiros - passageiros_de_fora

            self.passageiros = 45
            return(f"Apenas {conseguiram_entrar} dos {novos_passageiros} novos passageiros conseguiram entrar no ônibus, {passageiros_de_fora} ficaram de fora por falta de espaço.")

        else:
            self.passageiros += novos_passageiros
            return(f"Todos os {novos_passageiros} novos passageiros conseguiram entrar no ônibus.")
        
    def desembarcar(self, passageiros_saindo):
        if self.movimento == True:
            return(f"Não é possivel desembarcar no momento pois o ônibus está em movimento!")
        
        elif self.passageiros == 0:
            return(f"Não é possivel desembarcar no momento pois o ônibus já está vazio!")
        
        elif self.passageiros < passageiros_saindo:
            return(f"Há apenas {self.passageiros} passageiros no ônibus, não é possivel desembarcar {passageiros_saindo} passageiros.")

        else:
            self.passageiros -= passageiros_saindo
            return(f"{passageiros_saindo} desembarcaram do ônibus.")
        
    def acelerar(self):
        if self.movimento == False:
            self.movimento = True
            return("O ônibus começou a se mover.")
        else:
            return("O ônibus já estava em movimento.")

    def frear(self):
        if self.movimento == True:
            self.movimento = False
            return("O ônibus parou de se mover.")
        else:
            return("O ônibus já estava parado.")
        
onibus_escolar = Onibus()

print(onibus_escolar.acelerar())
print(onibus_escolar.frear())
print(onibus_escolar.embarcar(15))
print(onibus_escolar.acelerar())
print(onibus_escolar.embarcar(5))
print(onibus_escolar.frear())
print(onibus_escolar.embarcar(5))
print(onibus_escolar.embarcar(45))
print(onibus_escolar.acelerar())
print(onibus_escolar.frear())
print(onibus_escolar.desembarcar(20))
print(onibus_escolar.desembarcar(40))

# 15) Crie um classe que represente uma fila no banco. Cada cliente que chegar no banco deverá respeitar as regras do banco:
# Primeira pessoa a chegar deverá ser a primeira a ser atendida.
# Voce deverá manter um registro da idade das pessoas na fila.

# comportamentos:
# atender
# atender_com_prioridade a pessoa com mais de 60 anos que está esperando há mais tempo

class Fila:

    def __init__(self):
        self.fila = []       # FILA
        self.prioridade = [] # REGISTRO DE PRIORIDADE

    def adicionar(self, idade):
        if idade >= 60:
            self.fila.append(idade)
            self.prioridade.append(idade)
        else:
            self.fila.append(idade)

        return(f"Uma pessoa de {idade} anos entrou na fila.")
    
    def atender(self):
        if len(self.fila) == 0:
            return("Não já ninguém na fila.")
        
        atendido = self.fila[0]

        if atendido in self.prioridade:
            self.prioridade.remove(atendido)
        
        self.fila.remove(atendido)
        return(f"Uma pessoa com {atendido} anos foi atendida.")
    
    def dar_prioridade(self):
        if len(self.prioridade) == 0:
            return("Não há ninguém com mais de 60 anos na fila.")
        
        prioritario = self.prioridade[0]
        self.prioridade.remove(prioritario)
        self.fila.remove(prioritario)
        return(f"Uma pessoa com {prioritario} anos teve um atendimento prioritário.")
    
banco = Fila()

print(banco.adicionar(17))
print(banco.adicionar(25))
print(banco.adicionar(82))
print(banco.adicionar(56))
print(banco.adicionar(71))
print(banco.adicionar(36))

print(banco.atender())
print(banco.dar_prioridade())
print(banco.atender())
print(banco.atender())
print(banco.dar_prioridade())
print(banco.atender())
print(banco.atender())
print(banco.dar_prioridade())
print(banco.atender())
