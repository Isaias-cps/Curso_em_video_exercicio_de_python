"""Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while."""

print('Gerador de PA')
print('-=' * 15)
first = int(input('Digite o Primeiro termo da PA: '))
reason = int(input('Digite a Razão da PA: '))
term = first
cal = 1
while cal <= 10:
    print(f'{term} →', end='')
    term += reason
    cal += 1
print('Fim')
