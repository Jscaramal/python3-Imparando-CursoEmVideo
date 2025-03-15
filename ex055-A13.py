#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
pesoMaior = 0
pesoMenor = 0
for c in range(1, 6):
    peso = float(input(f'Digite o peso da pessoa {c}: '))
    if c == 1:
        pesoMaior = peso
        pesoMenor = peso
    else:
        if peso > pesoMaior:
            pesoMaior = peso
        elif peso < pesoMenor:
            pesoMenor = peso

print(f'O maior peso é {pesoMaior} e o menor é {pesoMenor}')
