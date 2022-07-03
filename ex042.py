"""refaça o desafio 035 dos triângulos, acresentando o recurso de 
mostrar que tipo de triângulo seŕ formado 
 Equilátero: Todos os lados iguais.
 Isósceles: Dois lados iguais.
 Escaleno: Todos os lados diferentes"""

sides1 = int(input('Digite o primeiro lado: '))
sides2 = int(input('Digite o segundo lado: ')) 
sides3 = int(input('Digite o terceiro lado: ')) 

if sides1 < sides2 + sides3 and sides2 < sides1 + sides3 and sides3 < sides1 + sides2:
    print('Os segmentos acima podem formar um triângulo!')
    if sides1 == sides2 == sides3:
        print(' O triâgulo formado é Equilátero')
    elif sides1 != sides2 != sides3 != sides1:
        print(' O triâgulo formado é Escaleno')
    else:
        print('O triângulo formado é Isósceles')
else:
    print('Os segmentos acima não porem formar um triângulo')