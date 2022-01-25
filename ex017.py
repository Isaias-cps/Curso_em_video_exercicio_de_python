"""Faça um programa que leia o comprimento do cateto opsto e do cateto adjacente 
de um triâgulo, calcule e mostre o comprimenda hipotenusa."""
from math import hypot 


side1 = float(input('Digite o valor do cateto oposto: '))
side2 = float(input('Digite o valor do cateto adjacente: '))
print(f'Com o valor do cateto oposto {side1} e o adjacente {side2} o valor da hipotenusa é {hypot(side1, side2) :.2f}')