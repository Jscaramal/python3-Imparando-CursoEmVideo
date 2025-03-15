# Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, moestre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada KM acima do limite

velocidade = float(input('Qual a velocidade atual do carro? km/h: '))
if velocidade > 80:
    print('Você foi multado por excesso de velocidade andando a {}km/h e o limite é de 80Km/h'.format(velocidade))
    print('O valor da multa é de R${:.2f}'.format((velocidade - 80) * 7))
else:
    print("Pode ir!! - Boa Viagem!")