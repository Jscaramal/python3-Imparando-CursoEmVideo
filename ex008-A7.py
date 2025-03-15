#Escreva um programa que leia um valor em metros e o exiba convertido em centimentros e milimetros.
print('Ciao! Calcolerò il valore che scegli da metri per centimetri e milimetri!')
metro = float(input('Inserisci un valore in metri: '))
print('Hai inserito il valore di {} in metro'.format(metro))
print('Allora, questo valore in centimetri è di {}'.format(metro *100))
print('Lo stesso valore in millimitri è di {}'.format((metro * 1000)))
print('A presto, caro!')