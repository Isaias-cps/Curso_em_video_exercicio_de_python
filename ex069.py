"""Crie um programa que leia a idade e o sexo de várias pessoas. a casa pessoa cadastrada, o programa 
deverá perguntar se o usuário quer ou não continuar. No final mostre:
Quantas pessoas tem mais de 18 anos 
Quantos homens foram cadastrados .
Quantas mulheres tem menos de 20 anos """

person = men = woman = 0 
while True:
    genre = ' '
    age = int(input('Digite a Idade da pessoa: '))
    while genre not in 'MF':
        genre = str(input('Qual é o gênero da pessoa[F/M]: ')).strip().upper()[0]
    if genre == 'M':
        men += 1
    if genre == 'F'and age < 20:
        woman += 1
    if  age > 18:
        person += 1
    answer = ' '
    while answer not in 'SN':
        answer = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if answer == 'N':
        break
print(f'Foram cadastrados {men} homens,')
print(f'Foran cadastradas {woman} mulheres com nemos de 20 anos')
print (f'Foram cadastradas {person} pessoas acima de 18 anos ')
