#crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = [[],[]]

for i in range(7):
    n = int(input(f'Digite o {i+1}° valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print(f'=-'*30)
print(f'A lista de pares é: {sorted(lista[0])}')
print(f'A lista de ímpares é: {sorted(lista[1])}')
print(f'=-'*30)