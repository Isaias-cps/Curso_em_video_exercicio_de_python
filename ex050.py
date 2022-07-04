"""Crie um programa que leie seis números inteiros
e mostre a soma apenas dequeles que forem pares. Se 
o valor digitado for impar desconsidere-o """

s = 0
cal = 0
for c in range(1, 7):
    numbre = int(input('Digite o número: '))
    if numbre % 2 == 0:
        cal += numbre
        s += 1
print(f'Você digitou: {s} números pares e a soma deles é: {cal}')

