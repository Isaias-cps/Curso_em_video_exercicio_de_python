""" Crir um programa que leia um npumero inteiro e diga se ele é ou não um número primo"""

number = int(input('digite um número: '))
cal = 0
for c in range(1, number +1 ):
    if number % c ==0:
        print('\033[33m', end=' ' '\n')
        cal += 1
    else:
        print('\033[31m', end=' ' '\n')
    print(c, end= ' ' )
print('\n')
print(f'\nO {number} foi divisivel {cal} vezes \n')
