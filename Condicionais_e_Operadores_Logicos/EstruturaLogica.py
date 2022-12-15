"""
Estruturas lógicas
"""

#and

sensor = 68

if sensor >= 60 and sensor <= 75:
    print('Tudo ok!')
else:
    print('Afaste-se!')

#or

pizza = True
lasanha = False

if pizza or lasanha:
    print('Preciso comer mais salada')
else:
    print('Estou com fome')

#is
login = False

if login is True:
    print('Logado')
else:
    print('Deslogado')