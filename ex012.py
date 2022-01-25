"""Crie um programa que leia o preço de um produto de mostre seu preço, com 5% de desconto."""


price = float(input('digite o valor do produto R$: '))
print(f'O valor do produto com 5% de desconto é: { price - (price * .05) :.2f}')