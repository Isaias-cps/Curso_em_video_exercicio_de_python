"""Crie um programa que vai gerar cinco números aleatórios e 
coçocr em uma tupla. depois, mostre a listagem de números
gerados e também indeque p menor eo maior valor que estão da tupla.  """
from random import randint

list_number = (randint(0, 10),randint(0, 10),randint(0, 10),
               randint(0, 10),randint(0, 10))
print('OS números gerados são: ', end='')
for n in list_number:
    print(f'{n}', end=' ')
print(f'\nO maior valor gerado foi {max(list_number)}')
print(f'O menor valor gerado foi {min(list_number)}')