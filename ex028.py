"""Crie um programa que sortei um número inteiro entre 0 a 5 e peça para o usuário tentar descobrir 
qual foi o número escolhido pelo programa. O programa deverá escrever na tela se o usuário venceu ou perdeu."""

from random import randint

print('O computador irar sortear um número de 0 a 5, tente acertar qual vai ser!')
number = int(input('Escolha um número: '))
drawn_number = randint(0, 5) 

if drawn_number == number:
    print('Você acertou o número, parabéns!')
else:
    print(f'O número sorteado foi:{drawn_number} e você escolheu {number} por isso você perdeu ')