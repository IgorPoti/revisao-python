#Exercício 003 - Referente aos tipos de variaveis e operacoes - Revisão Igor

print('----------Bem Vindo ao menu----------')
print('--------------Crie o seu personagem---------------')
cor_cabelo = input('Digite a cor do cabelo: ')
cor_pele = input('Digite a cor da pele: ')
classe = input('Digite a sua classe dentre:\n Guerreiro\n Mago\n Arqueiro\nOpcao: ')
idade = int(input('Digite sua idade em anos: '))
altura = float(input('Digite sua altura em metros: '))
habilidade_especifica = input('Digite sua habilidade: ')
print('---------------Personagem Criado----------------')
print(f'Seu personagem tem: \n'
      f'Cabelo de cor: {cor_cabelo}\n'
      f'Pele de cor {cor_pele}\n'
      f'Classe {classe}\n'
      f'Idade de {idade}\n'
      f'Altura de {altura}\n'
      f'Habilidade de {habilidade_especifica}')