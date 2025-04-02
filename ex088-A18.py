# faça um programa que ajude um jogador da mega sena a criar palpites. 
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
# cadastrando tudo em uma lista composta.
# Exemplo:
# Digite quantos jogos você quer que eu sorteie: 5
#  Sorteando 5 jogos de 6 números...
#  Jogo 1: 7 13 25 32 33 57
#  Jogo 2: 1 2 3 4 5 6 ...
from random import randint
from time import sleep as delay
#jogos = []
print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*30)
qtd_jogo = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*3, end='')
print(f' SORTEANDO {qtd_jogo} JOGOS ', end='')
print('-='*3)

for i in range(qtd_jogo):
    jogo = []
    while len(jogo) < 6:
        v = randint(1,60)
        if v not in jogo:
            jogo.append(v)
    jogo.sort()
    #jogos.append(jogo)
    print(f'Jogo {i+1}: {jogo}')
    delay(1)
print('-='*5, end='')
print(' < BOA SORTE! > ', end='')
print('-='*5, end='')

