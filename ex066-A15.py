# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
soma = cont = 0;
while True:
    n = int(input("Digite um valor (999 para parar): "))
    if n == 999:
        break
    soma += n
    cont += 1
print(f"Foram digitados {cont} números e a soma entre eles foi {soma}")