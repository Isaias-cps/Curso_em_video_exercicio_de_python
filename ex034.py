""" Crie um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superior a R$1.250,00 calcule um aumento de de 10%.
Para ps inferiores ou iguais, o aumento é de 15%."""

salary =  float(input('Informe seu salário: '))

if salary > 1250:
    print(f'O Salário de quem ganhava {salary} com o aumento vai para R$:{(salary * .1) + salary}')
else:
    print(f'O salário de quem ganhava {salary} com o aumento vai para R$:{(salary * .15) + salary}')