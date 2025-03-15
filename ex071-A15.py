#   Crie um progrma que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (numero inteiro) e o programa
#   vai informar quantas cédulas de cada valor serão entregues.
#   OBS: COnsidere que o caixa pussui cedulas de 50, 20, 10 e 1.

print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor = int(input('Que valor deseja sacar? R$ '))
c50 = c20 = c10 = c01 = 0
while True: #Notas de 50
    if valor >= 50:
        valor -= 50
        c50 += 1
    else:
        break
while True: #Notas de 20
    if valor >= 20:
        valor -= 20
        c20 += 1
    else:
        break
while True: #Notas de 10
    if valor >= 10:
        valor -= 10
        c10 += 1
    else:
        break
while True: #Notas de 01
    if valor >= 1:
        valor -= 1
        c01 += 1
    else:
        break
print(f'Total de {c50} de R$50\n' if c50 > 0 else '', end='')
print(f'Total de {c20} de R$20\n' if c20 > 0 else '', end='')
print(f'Total de {c10} de R$10\n' if c10 > 0 else '', end='')
print(f'Total de {c01} de R$01\n' if c01 > 0 else '', end='')
#print(f'Saldo restante: {valor}')
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')