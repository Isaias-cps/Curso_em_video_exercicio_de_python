"""Crie um programa que leia quatro valores pela teclado e 
guarde-os em uma tupla. No final, mostre:
Quantas vezes apareceu o valor 9.
Em que posição foi digitado o primeiro valor 3.
Quais foram os números pares."""

number = (int(input('Digite um número: ')),
          int(input('Digite outro número: ')),
          int(input('Digite mais um número: ')),
          int(input('Digite o último número: ')))
print(f'Os valores digitados foram {number}')
print(f'O valor 9 foi digitados {number.count(9)} vezes')
if 3 in number:
    print(f'A primeira posição que o valor 3 foi digitado foi {number.index(3) +1}ª4')
else:
    print('O valor 3 não foi digitado!')
print('Os valores pares digitados foram', end='')
for s in number:
    if s % 2 == 0:
        print(s, end=' ')