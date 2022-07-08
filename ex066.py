"""Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 777, que é a 
candição de parada. No final, mostre quantos números foram 
digitados e qual foi a soma entre eles [desconsiderando o flag]."""

number = sum = 0
while True:
    number = int(input('Digite um número para a soma [digite 777 para parar] :'))
    if number == 777:
        break
    sum += number
print(f'A soma dos valores foi {sum}')