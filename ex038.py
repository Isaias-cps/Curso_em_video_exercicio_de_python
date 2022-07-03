"""Crie um programa que leia dois números inteiros e compare-os
mostrando na tela uma mensagem:
-O primeiro valor é maior
- O segundo valor é maior 
- não existe valor maior , os dois são iguais"""

from operator import indexOf


number1 = int(input('Digite o primeiro valor: '))
number2 = int(input('Digite o segundo valor: '))

if number1 > number2:
    print(f'O primeiro valor é maior. {number1} é maior que {number2}')
elif number2 > number1:
    print(f'O segundo valor é maior. {number2} é maior que {number1} ')
else:
    print('Os valores são iguais')