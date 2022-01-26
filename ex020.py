"""Um professor quer sortear a ordem de apresentação de trabalhos dos alunos.
cria um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. """

from random import shuffle

name01 = input('Digite o nome do primeiro aluno: ')
name02 = input('digite o nome do segundo aluno: ')
name03 = input('digite o none do terceiro aluno: ')
name04 = input('digite o nome do quarto aluno: ')
list01 = [name01, name02, name03, name04]
shuffle(list01)
print(f'A ordem de apresentação é: {list01}')
