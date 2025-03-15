#faça um programa em python que abre e reprodua o audio de um arquivo mp3.


'''from playsound3 import playsound

print('Aproveite a musica :)')
playsound('C:/Users/Scaramal/Videos/0926.MP3')'''

import pygame
pygame.init()
pygame.mixer.music.load('0926.mp3')
pygame.mixer.music.play()
input(pygame.event.wait())