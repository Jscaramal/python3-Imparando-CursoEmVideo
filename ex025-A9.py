'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome'''

nome = str(input('Digite seu nome completo: '))
print(nome)
print('Seu nome tem Silva?', 'silva' in nome.lower().split())