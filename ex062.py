"""Merlhore o desafio 061, perguntando para o usuário se ele quer mostrar
mais alguns termos. O proframa encerra quando ele sisser que quer mostrar 0 termos"""



print('Gerador de PA')
print('-=' * 15)
first = int(input('Digite o Primeiro termo da PA: '))
reason = int(input('Digite a Razão da PA: '))
term = first
cal = 1
tot = 0
most = 10
while most != 0:
    tot +=  + most
    while cal <= tot:
        print(f'{term} →', end='')
        term += reason
        cal += 1
    print('Pausa')
    most = int(input('quantos termos você quer a mais? '))
print('Fim')
print(f'Progressão finalizada com {tot} termos mostrados')