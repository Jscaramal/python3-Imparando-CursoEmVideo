#Crie um programa que vai ler vários númerso e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
valores = []
r = 'S'
while r != 'N':
    valores.append(int(input('Digite um valor:')))

    while True:
        r = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
        if r in 'NS':
            break
        else:
            print('Opção inválida, tente novamente!')    
print('=-'*30)
print(f'Foram digitados {len(valores)} números.')
print(f'Os valores ordenados de forma decrescente {sorted(valores, reverse=True)}')
if 5 in valores:
    print(f'O valor 5 foi digitado e está na posição {valores.index(5)} da lista.')
else:
    print('O valor 5 não foi digitado.')
print('=-'*30)
print('FIM')
