# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
from time import sleep

op = 0
while(op != 5):
    print('Digite 2 numeros:')
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
    op= 0
    while(op != 5 and op != 4):
        print("""   O que deseja fazer?
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa""")
        op = int(input('Digite: '))
        if op == 1:
            print('A soma de {} + {} = {}'.format(n1, n2, n1 + n2))
        elif op == 2:
            print('A multiplicação de {} * {} = {}'.format(n1, n2, n1 * n2))
        elif op == 3:
            if n1 == n2:
                print(f'O número {n1} é igual ao número {n2}')
            elif n1 > n2:
                print(f'O número {n1} é maior que o número {n2}')
            else:
                print(f'O númerio {n1} é menor que o número {n2}')
        elif op == 4:
            print('|'*50)
        elif op == 5:
            print('Saindo do programa...')
            sleep(2)
        else:
            print('='*5)
            print('Opção inválida!!')
            print('='*5)
print("Fim do programa!")