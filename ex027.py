""" Crie um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro 
e o último nome separadamente.
Ex: Ana Maria de souza
primeiro: Ana 
útimo : Souza"""

name = input('Digite seu nome completo: ').strip()
list_name  = name.split()
print(f'Seu primeiro nome é: {list_name[0]}')
print(f'Seu útimo nome é: {list_name[-1]}')