"""Crie um programa que tenha uma tupla com várias pelavras
(não usar acentos). Depis disso, você deve mostrar, para cada
 palavras, quais são as suas vogais. """

words = ('aprender', 'programar', 'linguagem', 'python', 
         'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 
         'mercado', 'programador', 'futuro')
for p in words:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for l in p:
        if l.lower() in 'aeiou':
            print(l, end=' ')