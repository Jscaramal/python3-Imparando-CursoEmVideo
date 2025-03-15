#Refaça o Desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes


#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
print('=-='*30)
print('Insira o tamanho de 3 retas e eu te falarei se é possível formar um triângulo ou não!')
print('=-='*30)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
resultado = r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2
limpa = '\033[m'
vermelho = '\033[1;31m'
verde = '\033[1;32m'
azul = '\033[1;33m'
print(f' \033[1;32mSIM!!!\033[m A retas conseguem formar um triângulo: {vermelho}R1 = {r1}{limpa}, {verde}R2 = {r2}{limpa}, {azul}R3 = {r3}{limpa}' if resultado == True
      else f'Infelizmente essas retas não formam um triângulo: {vermelho}R1 = {r1}{limpa}, {verde}R2 = {r2}{limpa}, {azul}R3 = {r3}{limpa}')

if resultado == True:
    if r1 == r2 == r3:
        print('Seu triângulo é do tipo Equilátero, pois todos os lados são iguais.')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('Seu triângulo é do tipo Isósceles, pois apenas dois lados são iguais.')
    else:
        print('Seu triângulo é do tipo Escaleno, pois todos os lados são diferentes.')
else:
    print('FIM!')