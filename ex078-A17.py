#faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = []

for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
print('=-' * 30)
print(f'Você digitou os valores {valores}')
pMax = []
pMin = []
for c, v in enumerate(valores):
    if(v == max(valores)):
        pMax.append(c)
    elif(v == min(valores)):
        pMin.append(c)

print(f'\nO maior valor digitado foi {max(valores)} nas posições', end=' ')
for p in pMax:
    print(f'{p}... ', end='')
print(f'\nO menor valor digitado foi {min(valores)} nas posições ', end='')
for p in pMin:
    print(f'{p}... ', end='')

print('\nFIM')