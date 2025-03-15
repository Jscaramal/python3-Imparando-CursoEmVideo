# Desenvolva um programa que pergunte a distância de uma viagem em Km:
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
#e R$0,45 para viagens mais longas.

distancia = float(input('Digite a distância da viagem: Km '))
print(f'O valor da passagem para a distancia de {distancia}Km será \033[1;31mR${distancia * 0.50:.2f}\033[m' if distancia <= 200
      else f'O valor da passagem para a distancia de {distancia}Km sera \033[1;31mR${distancia * 0.45 :.2f}.\033[m')