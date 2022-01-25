"""Crie um programa que leia o salírio de um funcionário e mostre
seu novo salário, com 15% de aumento"""
salary = float(input('digite o salário do funcionário: '))
print(f'O salári do funcionário era {salary} com 15% de aumento vai para {(salary * .15) + salary}')