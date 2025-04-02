# Aprimore o desafio anteior, mostrando no final:
# a) A soma de todos os valores pares digitados.
# b) A soma dos valores da terceira coluna.
# c) O maior valor da segunda linha.

matriz = [[], [], []]

for i in range(3):
    for j in range(3):
        valor = int(input(f'Digite o valor para a matriz na posição [{i}][{j}]: '))
        matriz[i].append(valor)
print('=-'*30)
print('A matriz digitada foi:')
for i in range (3):
    for j in range (3):
        print(f'[ {matriz[i][j]} ]', end='')
    print()
print('=-'*30)

soma_pares = 0
soma_terceira_coluna = 0
maior_valor_segunda_linha = max(matriz[1])
for m in matriz:
    for n in m:
        if n % 2 == 0:
            soma_pares += n
    soma_terceira_coluna += m[2]
print(f'A soma dos valores pares é: {soma_pares}')
print(f'A soma dos valores da terceira coluna é: {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é: {maior_valor_segunda_linha}')