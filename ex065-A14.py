#crie um programa que leia varios número inteiros pelo teclado.
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lidos.
#o programa de ve perguntar ao usuário se ele quer ou não continuar a digitar valores.

soma = maior = menor = cont = 0
r = 'S'
while r not in 'Nn':
    n = int(input('Digite um número inteiro: '))
    if cont == 0:
        soma = menor = maior = n
    else:
        soma += n
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    cont += 1
    r = input('Quer continuar? [S/N] : ').strip()[0]
print(f'Foi digitado {cont} numeros. A média deles foi {soma / cont:.2f}. O maior foi {maior} e o menor foi {menor}!!')