"""crie um programa que leia vários números inteiros pelo tetaclado. 
O programa só vai parar quando o usuário digitar o valor 999, que
é condição de parada. No final, mostre quantos números foram
sigitados e qual foi a soma entre eles """
number = 0
calc = 0 
sum = -1
while number != 999:
    calc += number
    sum += 1
    number = int(input('Digite um número para somar [999 para parar]: '))       
print(f'Foram digitados {sum} Números e a soma entre eles é {calc}')