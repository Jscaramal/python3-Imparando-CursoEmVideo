#Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuario digitar o valor 999
#que é a condição de parada. No final. mostr quantos números foram digitados e qual foi a soma entre eles, desconsiderando o 999

num = 0
soma = 0
contador = -1
while num != 999:
    soma += num
    num = int(input("Digite um número inteiro: "))
    contador += 1
print(f"Fora digitados {contador} números e a soma deles é de {soma}!")