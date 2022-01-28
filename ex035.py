"""Crie um programa que leia o comprimento de três retas e diga ao usúario se elas podem ou não formar um triângulo."""


length1 = float(input('Digite o preimeiro comprimento: ')) 
length2 = float(input('Digite o segundo comprimento: '))
length3 = float(input('Digite o terceiro comprimento: '))
if length1 < length2 + length3 and length2 < length1 + length3 and length3 < length1 + length2:
    print('Com esses segmentos é possível formar um triângulo!')
else:
    print('Com esses Segmentos não é possível formar um triângulo.')