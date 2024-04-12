import advinhacao
import random

jogos = int(input("(1) Advinhação (2) Forca"))
if (jogos == 1):
    advinhacao.jogar()
elif (jogos == 2):
    forca.jogar