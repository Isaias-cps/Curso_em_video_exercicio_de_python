"""Crie um programa que leie seis números inteiros
e mostre a soma apenas dequeles que forem pares. Se 
o valor digitado for impar desconsidere-o """

s = 0
cal = 0
for c in range(1, 7):
    number = int(input('Digite o número: '))
    if number % 2 == 0:
        cal += number
        s += 1
print(f'Você digitou: {s} números pares e a soma deles é: {cal}')

