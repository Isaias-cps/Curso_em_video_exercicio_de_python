"""Crie um programa para aprovar empréstimo bancario para compra de casa.
Pergunte o valor da casa, e o salário do comprador 
e em quantos anos ele vai pagar. 
A prestação mensal, não poderá exceder 30% do salário ou então o então o emprestimo será negado. """


house_value = float(input('Qual o valor da casa? '))
payment_time = int(input('Em quantos anos pretende quitar a dívida? '))
salary = float(input('Digite sua renda mensal: '))


calculation = house_value / (payment_time * 12)

if calculation >= (salary * .3): 
    print(f'Infelismente com não poderemos fazer o emprestimo, valor das parcelas R$:{ calculation :.2f},\nSua parcela deve ser menor que R$:{(salary * .3) :.2f}')
else :
    print(f'Parabéns você é elegivel para um empréstimo Valor das parcelas R$:{calculation :.2f},\nNão ultrapasa o limite de 30% dos seus ganhos que são R$:{salary * .3 :.2f}  ')

