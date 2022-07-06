"""Crie um programa que leia dois valores e mostre um menu como ao lado na tela:
Seu programa deverá realizar a operação solicitada em cada caso
[1] Soma
[2] Multiplicar
[3] Qual é o mior
[4] Novos números
[5] Sair do programa 
    """
number_1 = int(input('Digite o primeiro número: '))
number_2 = int(input('Digite o segundo numero: '))
leave = 0
choice = 0

while leave != 5:
    print( 20  * '*')
    print('[1]Soma \n[2]Sultiplicação \n[3]Saber quem é o maior \n[4]Novos números \nSair do programa ')
    choice = int(input('Digite uma das opções: '))
    if choice == 4 or 2 or 1 or 3 :
        if choice == 1:
            print(f'A soma de entre {number_1} + {number_2} = {number_1 + number_2}')
        if choice == 2:
            print(f'A multiplicação entre {number_1} * { number_2} = { number_1 * number_2}')
        if choice == 3:
            if number_1 > number_2:
                print(f'O maior é {number_1}')
            elif number_1 < number_2:
                print(f'O maior é = {number_2}')
            else:
                print(f'O número {number_1} é igual a {number_2}')
    if choice == 4:
        number_1 = float(input('Digite o primeiro número novamente: '))
        number_2 = float(input('Digite o segundo numero novamente: '))

    if choice == 5:
        leave = 5
    else:
        print('Opção inválida')
    print(20 * '*')

print('fim')