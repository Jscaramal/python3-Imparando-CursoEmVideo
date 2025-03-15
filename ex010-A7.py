#Crie um programa que leia quanto dinheiro uma pessoa etm na carteira e mostre quantos Dólares ela pode comprar.
#US$1,00 = R$3,27

print('Calcolerò per te il cambio da BRL a USD.')
valore = float(input('Scrivi l’importo che hai nel portafoglio(in BRL): R$'))
tasso_di_cambio = 3.27
dollari = valore / tasso_di_cambio
print('Potresti comprare {:.2f} dollari americani.'.format(dollari))