#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou.
#Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será aguardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
from os import system
system('cls')
nome = str(input('Digite o nome do jogador: '))
qtdpartidas = int(input('Diginte o Nº de partidas: '))
jogador = {"nome": nome, "GolsPartidas": [], 'TotalGols': 0}
for i in range(qtdpartidas):
    gol = int(input(f"  Quantos gols o jogador {jogador["nome"]} fez na {i+1}ª partida: "))
    jogador["GolsPartidas"].append(gol)
jogador['TotalGols'] = sum(jogador['GolsPartidas'])
print('-='*30)
print(jogador)
print('-='*30)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador['nome']} jogou {len(jogador['GolsPartidas'])} partidas.')
for c,v in enumerate(jogador['GolsPartidas']):
    print(f'     => Na partida {c+1}, fez {v} gols.')
print(f'Foi um total de {jogador['TotalGols']} gols.')