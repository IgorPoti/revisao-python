"""
Estruturas condicionais
"""

# Testar altura para brinquedo do parque

altura = float(input('Digite a sua altura: '))

if altura < 1.6:
    print('Saia daqui')
else:
    print('Você pode brincar!')

# Consultar média final para aprovação

nota = float(input('Digite a sua nota:'))

if nota >= 6:
    print('Pode curtir suas férias')
else:
    print('Te vejo ano que vem outra vez')

# Determinar se um número é par ou ímpar

num = int(input('Digite um numero'))

if num % 2 == 0:
    print(f'{num} é par')
else:
    print(f'{num} é ímpar')

# Utilizando outros tipos de dados

# Strings

pais = input('Digite um país que você deseja visitar')

if pais == 'Noruega':
    print('Ah não, muito frio!')
elif pais == 'China':
    print('Ah não, muito longe')
elif pais == 'Australia':
    print('Ah não, muito canguru!')
else:
    print('Vamos!')

# Boolean

login = False
senha = 'Caneta 1'

key = input('Digite a sua senha:')

if key == senha:
    login = True
else:
    print('Senha incorreta!')

if login == True:
    print('Bem-vindo admin')
else:
    print('Tente novamente')




