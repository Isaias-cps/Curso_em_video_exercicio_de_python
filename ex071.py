"""Crie um programa que simule o funcionamento de um 
caixa eletrônico. No inicio, pergunte ao usuário qual 
será o valor da ser sacado (número imteiro) e o programa
 vai informar quantas cédulas de cada valor serão entregues
 cédulas de R$50, R$20 R$10 e R$1"""

valor = int(input('Qual o valor do saque? '))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} Cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break 
print('Saque terminado!!!')
