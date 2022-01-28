"""Crie um programa que leia a velocidade de um carro. Se ele utrapassar 80Km/h, mostre uma mensagem 
dizendo que ela foi multado. 
A multa vai custar R$7,00 por cada Km acima do limite."""


from multiprocessing.spawn import import_main_path


car = float(input('Digite a velocidade do carro: '))

if car > 80:
    print(f'Você foi multado, o valor da multa é R$: {(car- 80) * 7  :.2f}')

print('continue dirigindo com segurança')

