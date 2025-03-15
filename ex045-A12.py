#Crie um prorama que faça o computador jogar jokenpô com você.
from random import choice

print('='*10)
print('Vamos jogar Jo-Ken-Pô ???')
print('='*10)
print('Vou escolher primeiro...')
computador = choice(['pedra', 'papel', 'tesoura'])
print('Já escolhi... Agora escolha você, digite pedra, papel ou tesoura.')
jogador = str(input('Digite sua jogada: '))
cColor = '\033[31m'
jColor = '\033[32m'
clearColor = '\033[0m'

if jogador == 'pedra' or jogador == 'tesoura' or jogador == 'papel':
    if ((computador == 'pedra' and jogador == 'pedra')
        or (computador == 'tesoura' and jogador == 'tesoura')
        or (computador == 'papel' and jogador == 'papel')):
        computador = cColor + computador + clearColor
        jogador = jColor + jogador + clearColor
        print(f'Parece que impatamos, eu escolhi {computador} e você escolheu {jogador} também. Mas na próxima eu vencerei!')
    elif((computador == 'pedra' and jogador == 'tesoura' or computador == 'papel' and jogador == 'pedra') or (computador == 'tesoura' and jogador == 'papel') ):
        computador = cColor + computador + clearColor
        jogador = jColor + jogador + clearColor
        print(f'Venci! Escolhi {computador} e você escolheu {jogador}. Perdedor!')
    else:
        computador = cColor + computador + clearColor
        jogador = jColor + jogador + clearColor
        print('\033[42;30m##VENCEU!!##\033[m')
        print(f'Você deu sorte! Escolheu {jogador} enquanto eu escolhi {computador}')
else:
    jogador = jColor + jogador + clearColor
    print(f'Não tem {jogador} nesse jogo... Não sabe brincar! Até mais!')