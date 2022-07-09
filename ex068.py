""" Crie um programa que jogue par ou impar com o compytador. O jogo
só será interrompido quando o jogador perder, mostrando o total 
de vitórias consecutivas que ele conquistiu no final do jogo."""

from random import randint
victory = 0
print('jogo do par ou impar')
while True:
    number = int(input('Escolhar um número de [0 a 10]: '))
    computer = randint(0, 10)
    tot = number + computer
    choice = ' '
    while choice not in 'PI':       
        choice = str(input('Par ou impar? [P/I]: ')).strip().upper()[0]
    print(f' Seu número é {number} e o do computador {computer} e o total é {tot} ')
    print('DEU PAR' if tot % 2 ==0 else 'DEU IMPAR')
    if choice == 'P':
        if tot % 2 == 0:
            victory += 1
            print('Você ganhou!')
        else:
            print('você perdeu!')
            break
    elif choice == 'I':
        if tot % 2 == 1:
            print('Você ganhou! ')
            victory += 1
        else:
            print('Você perdeu! ')
            break 
    print('Vamos jogar novamente...')
print(f'GAME OVER! você venceu o total de vezes {victory}')
    
