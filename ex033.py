"""Crie um programa de leia três números e mostre qual é o maior e qual é o menor."""

from tokenize import Number


number1 = int(input('digite o primeiro número: '))
number2 = int(input('Digite o segundo número: '))
number3 = int(input('Digite o terceiro número: '))
minor = number1
if number2 < number1 and number2 < number3:
    minor = number2
if number2 < number1 and number3 < number2:
    minor = number3

more = number1
if number2 > number1 and number2 > number3:
    more = number2
if number3 > number1 and number3 > number2:
    more =  number3

print(f'O menor número digitado foi: {minor}')
print(f'O maior número digitado foi: {more}')


print(number3)