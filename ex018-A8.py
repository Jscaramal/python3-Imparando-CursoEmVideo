#Faça um programa que leia um ângulo qualquer e mostre na tela o balor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians

angulo = float(input('Digite um angulo: '))
anRadians = radians(angulo)
print('O angulo digitado foi {}º o Seno é {:.2f}, Cosseno {:.2f}, tangente {:.2f}'.format(angulo, sin(anRadians), cos(anRadians), tan(anRadians)))