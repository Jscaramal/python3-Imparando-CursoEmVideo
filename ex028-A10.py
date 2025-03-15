# Escreva um programa que faça o computador "pensar"
# em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o numero escolhido pelo computador
# O programa deverá escrever na tela se o usuário venceu ou perdeu
from random import randint


numeroRandomico = randint(0, 5)

numEscolhido = int(input('Em que número eu pensei? \n Digite um numero entre 0 e 5: '))
if numEscolhido > 5:
   print('Número maior que 5. :(')
else:
    print('Venceu!' if numEscolhido == numeroRandomico else "PERDEU MANÉ! O numero era {}".format(numeroRandomico))