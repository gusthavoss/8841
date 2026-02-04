# 17) Assuma que há uma empresa com varios sensores de temperatura espalhados por seu predio, que geram leituras constantes. O 
# sistema dessa empresa precisa processar essas leituras, filtrá-las e gerar um relatório.

# - Simular os sensores (Criar generators para a geração das leituras de temperatura em celcius.)
# - Filtrar as leituras inválidas (filter) (menor que -20°c e maior que 50°c)
# - Converter esses valores (map) pra um formato de fahrenheit
# - Gerar um relatório (reduce) pra:
#   - Temperatura media
#   - Temperatura maxima
# - Faça com que esse script não seja executado automaticamente em caso de importação.

# 18) Escreva um programa utilizando funções que realize um cadastro.
# Deverão ser coletadas as seguintes informações:

# CPF
# Nome
# Idade
# Sexo
# Cidade

# Os registros deverão ser armazenados em um arquivo CSV
# Para manter o padrão brasileiro, o CSV deverá utilizar o ";" como delimitador
# O programa deverá possuir uma função de colsulta (por nome ou cpf)
# O programa deverá possuir uma função de exclusão (por cpf)
# O programa deverá ter tratamento de erros, com a finalidade de que o programa nunca dê uma exceção, e também de que ele não 
# aceite dados incorretos/inválidos.
import random

temperatura = []

def gerar_temperatura(quantidade):
    
    for i in int(quantidade):
        temperatura[i]

gerar_temperatura(10)
print(temperatura)
