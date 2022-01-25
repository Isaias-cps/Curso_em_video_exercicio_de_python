"""Crie um programa que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelo quais ele foi alugado. Calcule o preço a pagar, sabendo 
que o carro custa R$60 por dia e R$0.15 por Km rodado."""


amount_day = int(input('Por quantos dia o carro foi alugado? ')) 
km = float(input('Qual foi a quilometragem rodada? '))
print(f'Carro a alugado por {amount_day} dia e {km} quilometros rodados o Proço do aluguel é R$:{(amount_day * 60) + (km * .15) :.2f} ')
