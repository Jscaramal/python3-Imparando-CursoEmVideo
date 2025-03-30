# Crie um programa que leia uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
matriz = [[], [], []]
for i in range(3):
    for j in range(3):
        v = int(input(f'Digite um valor para [{i},{j}]: '))
        matriz[i].append(v)
print('=-'*30)
print('A matriz digitada foi:')
for i in range(3):
    for j in range(3):
        print(f'[ {matriz[i][j]} ]', end='')
    print()
print('=-'*30)
print('Fim')