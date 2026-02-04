# Match Case -> pattern watching (Disponivel a partir do python 3.10)

def saudacao(nome):
    match nome:
        case "Gusthavo":
            return "Olá, Gusthavo"
        case "Caio":
            return "Olá, Caio"
        case _:
            return "Olá, estranho"

print(saudacao("Caio"))
print(saudacao("Gusthavo"))
print(saudacao("Zé"))


# for else -> Execurar um trecho de código após um loop for caso ele tenha executado até o fim

lista = [2, 4, 6, 8, 10, 12]

for numero in lista:
    if numero > 9:
        break
    print(numero)

else:
    print("Nenhum Break ocorreu durante a execução do for")

# Ambientes Virtuais -> Virtual Enviromment - venv
