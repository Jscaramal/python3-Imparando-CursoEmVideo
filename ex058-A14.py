# Melhore o jogo do desafio 028, onde o computador vai "pensar" em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites, foram necessário para vencer.
import random
from pygame.time import delay

print('=-'*40)
print('Eu vou pensar em um numero entre 0 e 10. Tente advinhar qual número eu pensei!...')
print('=-'*40)
numJogador = 11
numeroComputador = 12
count = 1
print("="*15)
print('Pensando...')
delay(2)
numeroComputador = random.randint(0,10)
while numeroComputador != numJogador:
    numJogador = int(input("Chute o número: "))
    if(numeroComputador == numJogador):
        print('#'*10)
        print(f'Acertou!')
        print('#'*10)
    else:
        print('#'*10)
        print(f'Errou!')
        print('#'*10)
        count += 1
        if(numJogador < numeroComputador):
            print('É mais!...')
        else:
            print('É menos!...')
print(f'Escolhi o numero {numeroComputador} e você disse o numero {numJogador}!')
print(f'Você precisou de {count} tentativas...')