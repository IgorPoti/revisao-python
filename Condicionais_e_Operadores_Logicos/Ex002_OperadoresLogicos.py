# Exercício 002 - Operadores Lógicos - Revisão João Igor


#1 - Crie um sistema de cadastro e login de um site, utilizando um username e
#senha informados pelo usuário.

login = False

print('Bem vindo ao meu site! \n Registre-se!')

usuario = input('Digite o nome do usuário: ')
senha = input('Digite a senha: ')

print('_______Login______')
if input('Usuário') == usuario and input('Senha') == senha:
    login = True

if login == True:
    print(f'Bem vindo(a), {usuario}')
else:
    print('Tente novamente!')