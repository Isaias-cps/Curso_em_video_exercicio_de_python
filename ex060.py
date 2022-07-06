"""Crie um programa que leia um número
qualquer e moster o seu fatorial."""

from calendar import c


number = int(input('Digite um número: '))
cal = number
fac = 1
print(f'Calculando {number}!=', end=' ')
while cal > 0 :
    print(f'{cal }' , end=' ')
    print(f'x' if cal > 1 else '=',end='')
    fac *= cal
    cal -= 1
print(f'{fac}')