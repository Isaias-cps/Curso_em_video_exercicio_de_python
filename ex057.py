""" Crie um programa que leia o sexo de uma pessoa, mas só aceita os valores 'M' ou 'F'.
Caso esteja essado, peça a digitação novamente até te um valor correto. """

enter = str(input('Digite qual é o sexo:[M]/[F]: ')).strip().upper()[0]
while enter not in 'MnFf':
    enter = str(input('Dado inválido.  Digite qual é o sexo:[M]/[F]: ')).strip().upper()[0]
print(f'Sexo {enter} registrado com sucesso')