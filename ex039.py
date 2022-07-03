"""Crie um programa que leia o ano de nascimento um jovem e informe,
de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, 
se é a hora de se alistar ou se ja passou do tempi do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. """


from datetime import date 
present = date.today().year
age = int(input('digite o ano de nascimento '))
calculation = present - age

if 2022 - age == 18:
    print(f'Esse ano você completa 18 anos de seu alistamento')
elif 2022 - age > 18:
    print(f'Você está um pouco atrasado seu ano de alistamento foi em {2022 - (calculation - 18)} há anos atrás:{calculation - 18} ')
else:
    print(f'Você ainda nãp pode se alistar seu ano e alistamento é em {2022 - (calculation - 18)} daquis há {18 - calculation} anos ')