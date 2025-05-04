# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: 
# o nome de um jogador e quantos gols ele marcou. 
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
from os import system
system('cls')


def ficha (nome = '', gols = "0"):
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    if nome.strip() == '':
        nome = '<desconhecido>'
    print('-'*30)
    print(f'O jogador {nome} fez {gols} gols(s) no campeonato.')
    
    

nome = str(input("Nome do Jogador: "))
gols = str(input("Número de Gols: "))


ficha(nome = nome, gols = gols)
