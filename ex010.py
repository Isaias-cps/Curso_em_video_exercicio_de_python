"""Crie um Programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre o quantos Dólares ela pode comprar.
considere US$1.00 = R$5.49"""

coin = float(input('quanto de dinheiro você tem na carteira, em Rais?: '))
print(f'A quantidade em Délares que você pode compra com R${coin}  é US${coin / 5.49 :.2f}  ')