"""Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todoa as letres maiúsculas e minúsculas.
Quantas letras ao todo (semcosiderar espaços 
Quantas letras tem o primeiro nome."""

from itertools import count


Name02 = input('Digite um nome completo: ')
print(f'O nome com letras ninúsculas: {Name02.lower()} nome com letras maiúsculas: {Name02.upper()}')
print('O nome tem {} de letras'.format(len(Name02) - Name02.count(' ')))
print('O primeiro nome tem {} letras'.format(Name02.find(' ')))