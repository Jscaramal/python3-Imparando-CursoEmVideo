#   Crie um progrma que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (numero inteiro) e o programa
#   vai informar quantas cédulas de cada valor serão entregues.
#   OBS: COnsidere que o caixa pussui cedulas de 50, 20, 10 e 1.

print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor = int(input('Que valor deseja sacar? R$ '))
ced = 50
total = valor
contadorCed = 0
while True:
    if total >= ced:
        total -= ced
        contadorCed += 1
    else:
        if contadorCed > 0:
            print(f'Total de {contadorCed} cedulas de R$ {ced}')
        contadorCed = 0
        if total >= 20:
            ced = 20
        elif total >= 10:
            ced = 10
        elif total >= 1:
            ced = 1
        if total == 0:
            break