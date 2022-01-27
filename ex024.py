"""Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra (santo)"""
city = input('Em qual cidade você nasceu? ').strip()
print(city[:5].upper() == 'SANTO')