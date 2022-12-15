# Exercício 001 - Operações condicionais - Revisão João Igor

#Fazer uma calculadora de 4 operações (soma, multiplicação, divisão inteira, potência).
#Peça a operação desejada e depois os dois números ao usuário.

print('Bem-vindo a calculadora, opções: \n 1- Soma \n 2- Multiplicação \n 3- Divisão inteira'
      '\n 4- Potência')
op = int(input('Selecione a opção:'))
num1 = float(input('Digite o primeiro número:'))
num2 = float(input('Agora digite o segundo número:'))

if op == 1:
    print(f'O resultado da soma é: {num1 + num2}')
elif op == 2:
    print(f'O resultado da multiplicação é: {num1 * num2}')
elif op == 3:
    print(f'O resultado da divisão inteira é: {num1 // num2}')
elif op == 4:
    print(f'O resultado da potenciação é: {num1 ** num2}')
else:
    print('Opção inválida, tente novamente')