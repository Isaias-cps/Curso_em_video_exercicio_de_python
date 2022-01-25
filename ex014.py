"""Escreva um programa que converta um temperatura digitada em °C e converta em °F."""


temperature = float(input('digite a temperatura em °C: '))
print(f'A temperatura de {temperature} em °C convertendo para °F fica {(1.8 * temperature) + 32} e em K {temperature + 273.15}')