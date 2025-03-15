#refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrano os 10 primeiros termos da progressão usando a estrutura while.

termo = int(input("Digite o primeiro termo da PA: "))
razão = int(input("Digite a razão da PA: "))
contador = 1
while contador <= 10:
    print(f'Termo {contador} : {termo}')
    termo += razão
    contador += 1