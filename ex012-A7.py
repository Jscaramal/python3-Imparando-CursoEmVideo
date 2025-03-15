#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
prezzoAttuale = float(input('Inserisci il prezzo atuale: €'))
prezzoScontato = prezzoAttuale - (prezzoAttuale * 0.05)
print('Ecco il nuovo prezzo scontato 5%: €{:.2f}'.format(prezzoScontato))