"""Crie um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos."""


comparator_smaller = 0
comparator_larger = 0

for c in range(0, 5):
    weight = float(input('Digite o peso da pessoa: '))
    if c == 0:
            comparator_larger = weight
            comparator_smaller = weight
    else:
        if weight < comparator_smaller:
            comparator_smaller = weight
        if  weight > comparator_larger:
            comparator_larger = weight
print(f'O maoir peso foi {comparator_larger} Kg e o menor foi {comparator_smaller} Kg')
