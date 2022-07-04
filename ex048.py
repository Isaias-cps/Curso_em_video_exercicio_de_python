""" faça um programa que calcule a soma entre todos os números
 impares que são multiplos de três e que se encontram no entervalo de 1 até 500"""


s = 0
con = 0

for c in range(1, 501, 2):
    if c % 3 ==0:
        con += 1
        s +=  c
print(f'A soma dos números divisível por 3 é {s} e a quantidade de vezes que apareceram foi {con} ')