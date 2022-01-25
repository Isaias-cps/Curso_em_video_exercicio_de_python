"""Crie um programa que leia a largura e altura de um parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintála,
sabendo que um livro de tinta, pinta uma área de 2 metros quadrados """


measure1 = float(input( 'Digite a largura da parede: ' ))
measure2 = float(input('Digite a altura da parede: '))
print(f'Com a largura de: {measure1} e altura de: {measure2} a área da parede é: {measure1 * measure2}')
print(f'A quantidade de tinta necessária para pinta é {(measure1 * measure2) / 2} litros')