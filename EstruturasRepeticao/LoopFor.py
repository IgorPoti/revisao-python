"""
Loop for

#Achando numeros pares dentro de uma sequencia

num = range(2,21)
for numero in num:
    if numero % 2 == 0:
        print(f'Achei um número par, numero: {numero}')

"""
heroi = 'Batman'
for valor in enumerate(heroi):
    print(valor)
for contador,letra in enumerate(heroi):
    print(f'A {contador+1} letra e:{letra}')
for valor in enumerate(range(3,7)):
    print(valor)
for contador,letra in enumerate(range(3,7)):
    print(f'O {contador+1} numero e: {letra}')
