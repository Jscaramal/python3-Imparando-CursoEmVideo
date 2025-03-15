#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
# e a quantidade de tinta necessária para pintá-la, saendo que cada litro de tinta, pinta uma área de 2m².
#1L = 2m²

print('Calcolerò la quantità di vernice necessaria per dipingere il muro.')
larghezza = float(input('Inserisci la Larghezza (in metri): '))
altezza = float(input('Inserisci l’altezza (in metri): '))
area = larghezza * altezza
litri = area / 2
print('Teu muro c’è {} m².'.format(area) )
print('Ecco la quantità di vernice necessaria per dipingere il muro: {:.2f} litri'.format(litri))