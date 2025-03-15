# faça um programa que jogue par ou impar com o computador. O jogo só será interrompindo quando o jogador PERDER,
#mostrando o total de vitórias consecutivas que ele conquistou no final do jogo
from random import randint

print('~'*25)
print('Vamos jogar PAR ou IMPAR?')
print('~'*25)
c = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Digite um valor: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou impar? [P/I] ')).strip().upper()[0]
    soma = computador + jogador
    parImpar = 'PAR' if soma % 2 == 0 else 'IMPAR' #verifica se a soma é par/impar e atribuí
    print(f"DEU {parImpar}")
    print('-'*30)
    print(f'Você jogou {jogador} e o computador {computador}. O Total de {soma} DEU {parImpar}')
    print('-'*30)
    if(escolha == parImpar[0]): # P=P or I=I
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        c +=1
    else:
        print('Você PERDEU!')
        break
    print('=-'*20)
print(f'GAME OVER! Você venceu {c} vezes')