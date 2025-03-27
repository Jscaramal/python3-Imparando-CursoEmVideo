# Crie um programa ond eo usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). 
# No final, mostre a lista ordenada na tela.

valores = []

for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if(c == 0):
        valores.append(num)
        print(f'Adicionado na posição {valores.index(num)}')
        continue
    for v in valores:
        if(num >= max(valores)):
            valores.append(num)
            print(f'Adicionado na posição {valores.index(num)}')
            break
        if(num < v):
            valores.insert(valores.index(v), num)
            print(f'Adicionado na posição {valores.index(num)}')
            break
print(f'Os valores digitados em ordem foram {valores}')
print('FIM')