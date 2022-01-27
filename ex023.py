"""crie um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
Ex: 
digite um número : 1834
unidade:4 dezena:3 centena:8 milher:1"""

num = int(input('Informe um número: '))
un = num // 1 % 10
dez = num // 10 % 10
cem = num // 100 % 10
mil = num // 1000 % 10
print(f'analizando o número {num}')
print(f'Unidade: {un}')
print(f'Dezena: {dez}')
print(f'Centena: {cem}')
print(f'Milhar: {mil}')
