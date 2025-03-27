#crie um programa que leia vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
#Ao final, mostre o conteúdo das três listas geradas.

valores = []

while True:
    
    valores.append(int(input('Digite um valor: ')))
    r = input('Deseja continuar [S/N]? ').upper().strip()[0]
    if r in 'NS':
        if r == 'N':
            break
        else:
            continue
    else:
        print('Opção inválida, tente novamente!')

pares = []
impares = []
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
        
print(f'Os valores digitados foram {valores}')
print(f'Os valores pares digitados foram {pares}')
print(f'Os valores ímpares digitados foram {impares}')
print('FIM')