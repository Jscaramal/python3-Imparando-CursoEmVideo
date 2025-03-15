#Faça um programa que converta uma temp digitada em ºC e converta para ºF
tempC = float(input('Qual è a temperatura em ºC: '))
tempF = (tempC * 9 / 5) + 32
print('A temperatura de {:.1f}ºC corresponde a {:.1f} ºF'.format(tempC, tempF))