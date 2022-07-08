"""Crie um programa que leia um número n inteiro qualquer e 
mostre na tela os n primeiros elementos de uma sequência de fibonacci. """

print( 30 * '-')
print('Sequêcia de Fibonacci')
number = int(input('Quantos termos você quer mostar?: '))
term1 = 0 
term2 = 1
print(30 * '~')
print(f'{term1} → {term2 }', end='')
calc = 3
while calc <= number:
    term3 = term1 + term2
    print(f' → {term3}', end='')
    term1 = term2
    term2 = term3
    calc +=1
print('→Fim')

