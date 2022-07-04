"""Refaça o exercicio 009, mostrando a tabuada de um número
 que o usuário escolher, só que agora utilizando o laço FOR"""

number = int(input('Digite um número para tabuada: '))

for c in range(1, 11):
    print(f'{number} X {c :2} = {number * c}')