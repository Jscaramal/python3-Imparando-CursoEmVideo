# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa
# o salário do comprador e
# em cquantos anos ele vai pagar.

#Calcula o valor da prestação mensal,
#sabendo que ela não pode exceder 30% do salário
#ou então o empréstimo será negado.

print('Olá, me diga as informações que vou te dizer se você pode comprar a casa!')
valorCasa = float(input('Digite o valor da casa: R$ '))
valorSalario = float(input('Digite o valor do seu salário: R$ '))
qtdParcela = int(input('Digite em quantos anos você irá pagar: '))
qtdParcela = qtdParcela * 12

print(f'Pelo que entendi, você quer uma casa no valor de R${valorCasa:.2f}, vai pagar em {qtdParcela:.0f} meses, e possui um salario de R${valorSalario:.2f}.')

valorPMensal = valorCasa / qtdParcela
if valorPMensal <= (valorSalario * 30 / 100):
    print('\033[42mSeu emprestimo foi aprovado com sucesso.\033[m')
    print(f'O valor da parcela é de R${valorPMensal:.2f}')
else:
    print(f'\033[41;30mInfelizmente o valor da parcela R${valorPMensal:.2f} ultrapassa 30% do seu salário que é R${valorSalario:.2f}\033[m')