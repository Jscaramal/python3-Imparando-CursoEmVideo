# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
# Guarde esses resultados em um dicionário. No final, coloque esses dicionários em ordem, sabendo que o vencedor tirou o maior número no dado
from random import randint
from time import sleep as delay
from operator import itemgetter
jogo = dict()
print('Valores sorteados:')
for i in range(4):
    jogo[f"jogador{i+1}"] = randint(1, 6)
for k,v in jogo.items():
    delay(0.5)
    print(f'{k} tirou {v} no dado.')
ranking = list()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*25)
print('== RANKING DOS JOGADORES ==')

for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]} pontos.')
    delay(0.5)
