# Exercicio 001 - Referente ao loop for - Revisão João Igor
"""
1 Faça um programa que calcule a soma dos divisores de um número inteiro
definido pelo usuário. Ex: Se o usuário escolheu 10, temos 1 + 2 + 5 + 10 = 18
"""

soma = 0
numero = int(input('Digite o número: '))

for num in range(1,numero+1):

    if numero % num == 0:

        soma = soma + num
print(soma)

"""
2 Faça um programa que imprima os n primeiros múltiplos de 5, sendo n definido
pelo usuário. Ex: Se o usuário escolheu n=3, será impresso 5,10,15.
"""
numero = int(input('Digite o numero de multiplos de 5 que deseja: '))
for num in range(1,numero+1):
    print(f'{5 * num}')