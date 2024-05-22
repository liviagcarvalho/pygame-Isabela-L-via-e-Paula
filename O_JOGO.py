import pygame
import random
import time

from inicio import*
from FASE1 import* 


levels = [1,2,3]

for i in levels:
    if i == 1: 
        show_start_screen()
        fase1 ()
        
        if K == 1:
            fase2()
            # igual fase 1 so que maia rapido

    if i == 2:
        if K == 2: 
            fase3()
            # igual fase 2 so que mais rapido 

    if i == 3:
        if K == 3:
            #tela de voce ganhou 
        

