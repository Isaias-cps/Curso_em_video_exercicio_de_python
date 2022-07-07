"""Crie um programa que leia vários números inteiros pelo teclado. No
final da ececução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""
calc= amount = larger = smaller = 0
reply = 'S'
while reply in 'Ss':
    number = int(input('Digite um número: '))
    calc += number
    amount += 1
    if amount == 1:
        larger = smaller = number
    else:
        if number > larger:
            larger = number
        if number < smaller:
            smaller = number 
    reply = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
print(f'Você digitou {amount} números e a média é {calc/ amount}')
print(f'O maior numero foi {larger} e o menor foi {smaller}')