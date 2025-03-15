#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

#Quantos dias alugados? 8
qtsDias = float(input('Quantos dias alugados? '))
kmRodado = float(input('Quantos Km rodados? '))
valorDiaria = qtsDias * 60
valorKm = kmRodado * 0.15
total = valorDiaria + valorKm
print('O total a pagar é de R${:.2f}'.format(total))