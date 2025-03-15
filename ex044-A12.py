#Elabora um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# A vista dinheiro/cheque: 10% desconto
# a vista no cartão: 5% de desconto
#ate 2x no cartão: preço normal
#3x ou mais no cartão: 20% dejuros

preco = float(input('Insira o preço do produto: R$ '))
pagamento = int(input(' Digite 1 para A vista dinheiro/cheque | Digite 2 para a vista no cartão '
                      '| Digite 3 para parcelar! \nOpção: '))
if pagamento == 3:
    parcela = int(input('Em quantas vezes deseja parcelar?\n'))
    if parcela <= 2:
        print(f'Parcelando em {parcela}x o preço será {parcela} x R$ {preco/parcela} = TOTAL R$ {preco}')
    elif parcela >= 3:
        preco = preco + (preco * 20 / 100)
        print(f'Parcelando em {parcela}x o preço será {parcela} x R$ {preco/parcela} = TOTAL R$ {preco}')
elif pagamento == 2:
    preco = preco - (preco * 5 / 100)
    print(f'O preço é R$ {preco} e terá um disconto de 5% = TOTAL R$ {preco}')
elif pagamento == 1:
    preco = preco - (preco * 10 / 100)
    print(f'O preço é R$ {preco} e terá um disconto de 5% = TOTAL R$ {preco}')