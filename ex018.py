""" Crie um programa que leia um ângulo e mostre na tela o valor 
do seno, conseno e tangente desse ângulo."""

from math import sin, cos, tan, radians

angle = float(input('Digite um ângulo: '))
print(f'O valor desse ângulo aplicando seno é {sin(radians(angle)) :.3f} e coseno é {cos(radians(angle)) :.3f} e tangente é {tan(radians(angle)) :.3f} ')