# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint


print(f'Os números sorteados foram: ', end='')
tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(tupla)
print(f'O maior número sorteado foi {max(tupla)}')
print(f'O menor número sorteado foi {min(tupla)}')