"""Crie um programa que leia um ano quaquer e mostre se ele é BISSEXTO."""


from datetime import date

ano = int(input('que ano quer analisar? '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} não é BISSEXTO')  