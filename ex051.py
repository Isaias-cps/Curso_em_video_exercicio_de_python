""" Crie um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiro termos dessa progressão."""

first = int(input('Digite o Primeiro termo da PA: '))
reason = int(input('Digite a Razão da PA: '))
b = {}
n = first + (10 -1) * reason
for c in range(first, n + reason, reason):
    print( c, end=' ')

    