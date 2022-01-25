"""crie um programa que leia um número real qualquer e mostre na tela a sua porção inteira 

Ex: digite um número: 6.127
O número 6.127 tem a parte inteira 6."""

from math import trunc




number = float(input('digite um número: '))
print(f'O número {number} tem a parte inteira {trunc(number)}')

#essa é uma outra forma de comtruir sem usar módulo

number = float(input('digite um número: '))
print(f'O número {number} tem a parte inteira {number :.0f}')