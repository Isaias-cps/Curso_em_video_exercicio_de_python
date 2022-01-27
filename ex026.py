"""Crie um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra "A".
Em que posição ela aparece a primeira vez.
Em que posição ela aparece a útima vez."""

digite = input('Digite uma frase: ').upper().strip()
print('A letra A aparece {} vezes na frese. '.format(digite.count('A')))
print('A primeira letra A apareceu na posição {}'.format(digite.find('A') + 1 ))
print('A útima letra A apareceu na posição {}'.format(digite.rfind('A')+ 1 ))