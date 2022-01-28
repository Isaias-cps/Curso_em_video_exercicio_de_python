"""Escreva um programa que leia uma valor em metros e exiba convertido em centimetro e milimetro"""


length = float(input('Escreva um valor em metros: '))
print(f'Esse valor em metros: {length}m \nCorresponde a esse valor em centrimentro: {length * 100 :.0f}cm \nE a esse valor em milimetro: {length * 1000 :.0f}mm ')
