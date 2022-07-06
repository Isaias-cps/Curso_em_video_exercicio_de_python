""" Melhore o jogo do Desafio 028 onde o computador vai 
"escolher" em um número entre 0 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
 quantos palpites foram necessarios para vencer.
  """

from random import randint

print('O computador irar sortear um número de 0 a 10, tente acertar qual vai ser!')

drawn_number = randint(0, 11) 
number = int
cal = 0
while number != drawn_number:
    cal += 1
    number = int(input('Escolha um número: '))
    if drawn_number == number:
        print('Você acertou o número, parabéns!')
    if number < drawn_number:
        print('Tente um pouca acima')
    if number > drawn_number:
        print('Tente um pouca abaixo') 
print(f'O número de tentativas foram {cal} ')
