import tkinter as tk
from PIL import Image
from MoverTabuleiro  import moverTabuleiro

def testaMoverTabuleiro(n): # teste a função na n+1-ésima posição
    i = 0
    while (i < n):
        moverTabuleiro() # no futuro 'n' pode ser útil para determinar número de rodadas/turnos da partida
        i+=1
    return

#testaMoverTabuleiro(3) 