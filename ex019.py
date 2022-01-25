"""Um professor quer sortear um dos quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido. """


from html.entities import name2codepoint
from random import choice

Name1 = input('Escreva o nome do primeiro aluno: ')
Name2 = input('Escreva o nome so segundo aluno: ')
Name3 = input('Escreva o nome do terceiro aluno: ')
Name4 = input('Escreva o nome do quarto aluno: ')
list1 = [Name1, Name2, Name3, Name4]
print(f'O aluno escolhico foi {choice(list1)}')