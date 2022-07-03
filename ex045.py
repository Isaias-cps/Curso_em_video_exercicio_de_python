"""Crie um programa que faça o computador jogar Jakenpô contra você."""

from lzma import FORMAT_ALONE
from time import sleep

from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('Suas Opções:\n [ 0 ] PEDRA\n [ 1 ] PAPEL\n [ 2 ] TESOURA')

jogador = int(input('EScolha uma jogada: '))
print('JO')
sleep(1)
print('ken')
sleep(1)
print('Pô')

print(f' o computador jogou: {itens[computador]}')
print(f'O Jogador Jogou {jogador} ')

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')    
    else:
        print('JOGADA INVALIDA!')
if computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')    
    else:
        print('JOGADA INVALIDA!')
if computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')    
    else:
        print('JOGADA INVALIDA!')
