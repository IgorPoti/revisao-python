#Exercício 003 - Referente a operações matemáticas dentro do Python - Revisão João Igor


#1 - Realizar média de 4 alunos

aluno01 = float(input('Insira a nota do aluno 01'))
aluno02 = float(input('Insira a nota do aluno 02'))
aluno03 = float(input('Insira a nota do aluno 03'))
aluno04 = float(input('Insira a nota do aluno 04'))

mediaAlunos = ((aluno01 + aluno02 + aluno03 + aluno04) / 4)

print(f'A média dos alunos da turma é {mediaAlunos}')



#2 - Converter uma temperatura de graus °C para ºF e para K

tempC = float(input('Temperatura em ºC: '))
tempF = tempC * 1.8 + 32
print(f'A temperatura em ºF é: {tempF}ºF\n')

tempK = tempC + 273.15
print(f'A temperatura em K é: {tempK}K')
