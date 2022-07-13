"""Crie um programa que tenha um tupla totalmente preenchida com uma contagem por extensã, de zero até vinte.

Seu programa deverá ler um npumero pelo teclado ( entre 0 e 20) e mostrá-lo por extenso."""


count = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
         'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 
         'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 
         'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    number = int(input('Digite um número entre 0 e 20: '))
    if 0 <= number <= 20:
        break
    print('Erro!!! número digitado fora do escopo. ', end='')
print(f'O número por extenso é {count[number]}')