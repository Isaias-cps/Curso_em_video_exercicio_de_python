"""Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
média abaixo de 5.0: Reprovado
Média entre 5.1 e 6.9: recuperação 
Média 7.0 ou acima: Aprovado"""

grade1 = float(input('Digite a primeira nota: '))
grade2 = float(input('Digite a segunda nota2: '))
average = (grade1 + grade2) / 2 

if  average >= 5.1 and average <= 6.9:
    print(f'Sua média é {average} e você está de recuperação')
elif average >= 7 and average <= 10:
    print(f'Parabéns sua nota foi: {average} você foi aprovado')
else:
    print(f'Sua nota foi: {average} e você foi reprovado')