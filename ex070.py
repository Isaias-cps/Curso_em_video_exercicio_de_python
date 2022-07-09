"""Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar. No final mostre:
Qual é o tatal de gasto na compra. 
Quantos produtos custam mais de R$1000.
Qual é o nome do produto mais barato.
 """





tot = 0
while True:
    product = str(input('Qual o nome do produto: '))
    price = float(input('Qual o valor do produto: '))
    if tot == 0:
        product_cheap = product
        price_cheap = price
        product_ex = 0
    tot += price
    if price >= 1000:
        product_ex += 1
    if  price < price_cheap :
        product_cheap = product
        price_cheap = price
    answer = ' '
    while answer not in 'SN':
        answer = str(input('Quer continuar? [S/N]: ')).strip().upper()[0] 
    if answer =='N':
        break
print(f'O total da compra foi R${tot}')
print(f'Teve produtos {product_ex} mais a cima de R$1000')
print(f'O produto mais bataro fou {product_cheap} com o preço de R${price_cheap}')