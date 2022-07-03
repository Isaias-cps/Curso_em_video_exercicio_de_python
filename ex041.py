"""A confederação nacional de natação precisa de um programa que leia
 o ano de nascimento de um atleta e mostre sua categoria, de acordo com sua idade
 Até 9 anos: Mirim
 Até 14 anos: infantil
 Até 19 anos junior
 até 25 anos Sénior
 Acima e 25 : Master"""

from datetime import date
present = date.today().year

age = int(input('digite o ano de nascimento '))
calculation = present - age

if calculation <= 9:
    print(f'Com a idade de {calculation} a categoria é Mirim')
elif calculation <= 14:
    print(f'Com a idade de {calculation } a categoria é Infantil')
elif calculation <= 19:
    print(f'Com a idade de {calculation } a categoria é Junior')
elif calculation <= 25:
    print(f'Com a idade de {calculation } a categoria é Sénior')
else :
    print(f'Com a idade de {calculation } a categoria é Master')
