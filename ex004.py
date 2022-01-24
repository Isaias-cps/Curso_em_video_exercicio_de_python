"""Faça um programa que leia algo pelo teclado e mostre na tela
o seu tipo primitivo e todoas as informaçõespossiveis sobre ela"""

any  = input('digite algo: ')
print('O tipo primitivo desse valor é ', type(any))
print('só tem spaços? ', any.isspace())
print('É um némero? ', any.isnumeric())
print('É alfabetico? ', any.isalpha())
print('É alfanumérico? ', any.isalnum())
print('está em maiúscula? ', any.isupper())
print('Está em minuscula? ', any.islower())