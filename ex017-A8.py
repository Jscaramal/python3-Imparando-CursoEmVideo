#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo  retangulo. calcule e mostre o comprimento da hipotenusa.
from math import hypot

catetoOposto= float(input('Digite o valor do cateto oposto: '))
adjacenteOposto= float(input('Digite o valor do adjacente: '))
hipotenusa= hypot(catetoOposto,adjacenteOposto)
print('O valor da hipotenusa é: {:.2f}'.format(hipotenusa))