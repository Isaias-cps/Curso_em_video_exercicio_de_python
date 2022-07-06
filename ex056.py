"""Crei um programa que leia o nome, idade e sexo de quatro pessoas. 
No final do programa, mrostre:
A média de iadade do grupo.
Qual é o nome do homem mais velho .
quantas mulheres têm menos de 20 anos"""

men = 0
woman = 0
name_m = ''
cal = 0
for c in range(0, 4 ):
    group = int(input('Digite a idade da pessoa: '))
    name = str(input('Digite o nome da pessoa: '))
    gender  = str.upper(( input('digite o sexo da pessoa [M]/[F]: ')))
    cal += group 
    if c == 0 and gender == 'M':
        men = group
    if group < 20 and gender == 'F':
        woman += 1
    if group >= men and gender == 'M':
        men = group
        name_m = name
    print('***********************')
print(f'O nome do homem mais velho é {name_m} e sua idade: {men} anos ')
print(f'A quantidade de  mulheres abaixo dos 20 são: {woman}')
print(f'A média das idades do grupo é: {cal / 4} anos')


