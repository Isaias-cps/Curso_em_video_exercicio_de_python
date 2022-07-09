"""Faça um programa que mostre a tabuada de vários números , un de 
casa vez, para cada valor digitado pelo usuário. O programa será 
interrrompido quando o número solicitado for negativo. """


while True:
    calc = 1
    count = 10
    number = int(input('Digite o número para ver sua tabuata: '))
    if number < 0:
        break
    while count >= 1:
        print(f' {number} x {calc :2} = {number * calc} ')
        calc += 1
        count -= 1
print('Fim do Programa! ')