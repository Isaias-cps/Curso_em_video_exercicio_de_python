""" Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:
À vista dinheiro/Cheque: 10% de desconto
À vista no cartão: 5% de desconto
Em até 2x no cartão: preço normal
3x ou mais no cartão: de juros """

product = float(input('Qual é o preço do produto?:'))
print('Digide 1 para pagamento em Dinheiro/Cheque')
print('Digide 2 para pagamento em Cartão')
form = int(input('Qual será a forma de pagamento?')) 

if form == 2:
    portion = int(input('Em quantas parcelas vai ser feito o pagamento? '))
    if portion == 1:
        print(f'O preço do produto será {product - (product * .05)}')
    elif portion == 2:
        print(f'O preço do produto será {product}')
    else:
        print(f'O preço do produto será {product + (product * .2)}')
elif form == 1:
    print(f'O preço do produto será {product- (product * .1)}')

