"""Crie um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
-1 para Binário
-2 para Octal
-3 para Hexadecimal
"""

number = int(input('Digite um número: '))
print('Digite umadas Opçẽos\n -1 para Binário\n -2 para Octal\n -3 para Hexadecidmal')
option = int(input('Escolha a sua opição:'))

if option == 1 :
    print(f'O número: {number} em Binario é: {bin(number)[2:]}')
elif option == 2:
    print(f'O número: {number} em Octal é: {oct(number )[2:]}')
elif option == 3:
    print(f'O número: {number} em Hexadecimal é: {hex(number)[2:]}')

