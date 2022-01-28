"""Crie um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, combrando R$0.50 por Km para viagens 
de até 200Km e R$0.45 para viagens mais longas"""

Km = float(input('digite a distância da viagem em Km: '))
if  Km <= 200:
    print(f'Sua viagem é de Km{Km} e o valor de é R$:{Km * .50 :.2f}')
else:        
    print(f'Sua viagem é de Km{Km} e o valor de é R$:{Km * .45 :.2f}')

