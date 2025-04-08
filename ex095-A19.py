# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
from os import system
system('cls')
time = []
jogador = {}
while True:
    jogador.clear()
    nome = str(input('Digite o nome do jogador: '))
    qtdpartidas = int(input('Diginte o Nº de partidas: '))
    jogador['nome'] = nome
    jogador['GolsPartidas'] = []
    jogador['TotalGols']= 0
    for i in range(qtdpartidas):
        gol = int(input(f"  Quantos gols o jogador {jogador["nome"]} fez na {i+1}ª partida: "))
        jogador["GolsPartidas"].append(gol)
    jogador['TotalGols'] = sum(jogador['GolsPartidas'])
    time.append(jogador.copy())
    while True:
        continua = str(input('Quer continuar [S/N]')).strip().upper()[0]
        if continua in 'SN':
            break
        print('Opçao inválida. Digite apenas S ou N.')
    if continua == 'N':
        break
print('-='*30)
#print(time)
print('-='*30)
print(f'{"cod":<5}', end='')
print(f'{"nome":<25}', end='')
print(f'{'gols':<25}', end='')
print('total', end='')
print()
print('--'*30)
for c, jogador in enumerate(time):
    print(f'{f'{c}':<5}', end='')
    print(f'{f'{jogador['nome']}':<25}', end='')
    print(f'{f'{jogador['GolsPartidas']}':<25}', end='')
    print(f'{f'{jogador['TotalGols']}':<2}', end='')
    print()
print('=-'*30)
while True:
    while True:
        j = int(input(('Mostrar dados de qual jogador? (999 para parar) ')))
        if j == 999:
            break
        elif j < len(time) and j >= 0:
            break
        else:
            print('Jogador não existe.')
    if j == 999:
        break
    print('##'*30)
    print(f'-- LEVANTAMENTO DO JOGADOR {time[j]['nome']}:')
    print('--'*30)
    for jogo, gols in enumerate(time[j]['GolsPartidas']):
        print(f'No jogo {jogo+1} fez {gols} gols.')
    print('##'*30)
print('<<< VOLTE SEMPRE >>>')
