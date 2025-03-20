# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
import random

numero = [0, 0, 0, 0, 0]

print(f'Os números sorteados foram: ', end='')
for i in range(5):
    numero[i] = random.randint(1, 10)
    print(numero[i], end=' ')
tupla = (numero[0], numero[1], numero[2], numero[3], numero[4]) 
print(f'\nO maior número sorteado foi {sorted(tupla)[-1]}')
print(f'\nO menor número sorteado foi {sorted(tupla)[0]}')