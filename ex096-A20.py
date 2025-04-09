#Faça um programa que tenhauma função chamada area(), que receba as dimensões de um terretno retangular (largura e comprimento) e mostre a área do terreno.
from os import system
system('cls')

def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terrrno de {largura}x{comprimento} é de {a}m².')
    

print('Controle de Terreno')
print('-'*30)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)