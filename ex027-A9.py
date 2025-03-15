'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
ex. Ana maria de souza
Primeiro = Ana
ultimo = Souza
'''

nomeCompleto = input('Digite seu nome completo: ').title().strip()
print('Primeiro: {}' .format(nomeCompleto.split()[0]))
print(f'Ultimo: {nomeCompleto.split()[-1]}')
