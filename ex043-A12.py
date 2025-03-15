# Desenvolva uma lógica que leia o peso e a altura de uma pessoa. calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

#Abaixo de 18.5: Abaixo do peso
#Entre 18.5 e 25: peso ideal
#25 até 30: sobrepeso
#30 até 40:Obesidade
# Acima de 40: Obesidade morbida

peso = float(input('Digite o peso em Kg: '))
altura = float(input('Digite sua altura em m: '))

imc = peso / (altura * altura )
if imc < 18.5:
    print(f'Você está abaixo do peso! Com um IMC de {imc:.2f}%. Parametro 18.5 a 25 ')
elif imc <= 25 :
    print(f'Você está no peso ideal! Parabéns! IMC de {imc:.2f}%. Parametro 18.5 a 25')
elif imc <= 30 :
    print(f'Você está com sobrepeso! IMC de {imc:.2f}%. Parametro 18.5 a 25')
else:
    print(f'Obesidade mórbida! Está com um IMC de {imc:.2f}%. Parametro 18.5 a 25')