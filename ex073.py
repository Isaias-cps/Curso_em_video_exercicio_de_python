"""Crie um atupla preenchida com 20 primeiros colocados 
da tabela do compeonato brasileiro de futebol, na ordem de colocação.
Depois mostre
OS 5 primeiros. 
Os últimos 4 colocados.
Time em ordem alfabética.
Em que pisição está o Bragantino """

t = ('Palmeiras', 'Corinthians', 'Internacional', 'Atletico-MG', 'Fluminense', 'Athletoco-PR',
     'Sãp Paulo', 'Santos', 'Flamengo', 'Botafogo', 'Bragantino', 'Goiás', 'Cuiabá',
     'Coritiba', 'América-MG', 'Avaí', 'Ceará-SC', 'Atlético-GO', 'Juventude', 'Fortaleza')
print('-=' * 35)
print(f'Lista de times do Brasileirão: {t}')
print('-=' * 35)
print(f'Os primeiros 5 colocados: {t [0:5]}')
print('-=' * 35)
print(f'O 5 últimos colocados: {t [-4:]}')
print('-=' * 35)
print(f'Times em ordem alfabética: {sorted(t)}')
print('-=' * 35 )
print(f'O Bragantino está na {t.index("Bragantino") +1}ª posição')