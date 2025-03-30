# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

maisPeso = list()
menosPeso = list()
dados = list()
contador = 0
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Digite um peso: ')))
    contador += 1
    if len(maisPeso) == 0:
        maisPeso.append(dados[:])
        menosPeso.append(dados[:])
    else :
        if dados[1] > maisPeso[0][1]:
            maisPeso.clear()
            maisPeso.append(dados[:])
        elif dados[1] == maisPeso[0][1]:
            maisPeso.append(dados[:])
        if dados[1] < menosPeso[0][1]:
            menosPeso.clear()
            menosPeso.append(dados[:])
        elif dados[1] == menosPeso[0][1]:
            menosPeso.append(dados[:])
    print('=-'*30)    
    dados.clear()
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('=-'*30)
print(maisPeso)
print(menosPeso)
print(f'Ao todo, você cadastrou {contador} pessoas.')
print(f'\nO maior peso foi {maisPeso[0][1]} dos seguintes: ', end='')
for i in maisPeso:
    print(f'{i[0]}', end=' ')
print(f'\nO menor peso foi {menosPeso[0][1]} dos seguintes: ', end='')
for i in menosPeso:
    print(f'{i[0]}', end=' ')


