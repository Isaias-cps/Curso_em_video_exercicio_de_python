"""Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Pina' no nome."""
nome = input('Digite seu nome completo: ')
print('Seu nome tem Pina? {}'.format('pina' in nome.lower()))
