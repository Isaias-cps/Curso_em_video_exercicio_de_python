""" Crie um programa que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
A abaixo de 18.5 Abaixo do peso
Entre 18.6 e 25: Peso ideal 
25.1 até 30: Sobrepeso
30.1 até 40: Obesidade
Acima de 40: Obesidade mórbida"""

weight = float(input('Digite o peso da pessoa: '))
height = float(input('Digite a altura da pessoa: '))
calculation = weight / (height ** 2)

if calculation < 18.5:
    print(f'O IMC é {calculation :.2f} Está abaixo do peso')
elif calculation >= 18.6 and calculation <= 25:
    print(f'O IMC é {calculation :.2f} Está no peso ideal')
elif calculation >= 25.1 and calculation <= 30:
    print(f'O IMC é {calculation :.2f} Está com Sobrepeso')
else:
    print(f'O IMC é {calculation :.2f} Está com Obesidade mórbida')