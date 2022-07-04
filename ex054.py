""" Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores"""
from datetime import date 
present = date.today().year
totmaior = 0
totmenor = 0
for c in range(0, 7):
    data = int(input('Digite o ano de nascimento: '))
    idade = present - data
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmenor} menores de idade e {totmaior} maiores e idade ') 
      


        
        

