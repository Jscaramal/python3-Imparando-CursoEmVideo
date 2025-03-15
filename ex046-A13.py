# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 seg entre eles
import sys
import tkinter
from time import sleep
from tkinter import messagebox, Tk

root = Tk()
root.withdraw()
print('#'*45)
print('CONTAGEM REGRECIVA PARA OS FOGOS DE ARTIFÍCIO')
print('#'*45)
  # Força a atualização imediata
print(f"⏳ Contagem regressiva: ")
for c in range(45, -1, -5):
    sys.stdout.write("\r"+ "#" * c)
    sleep(1)


messagebox.showinfo("Fireworks!",'''      *        *    .        *  
  *        *        .      *  
      *  💥 BOOM 💥  *  
  *        *        .      *  
      *        *    .        *  
''')
print('''      *        *    .        *  
  *        *        .      *  
      *  💥 BOOM 💥  *  
  *        *        .      *  
      *        *    .        *  
''')
