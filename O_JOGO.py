import pygame
import random
import time

from inicio import*
from Fase1 import* 
from Fase2 import*
from Fase3 import*
from salvou_reino import*


levels = [1,2,3]

K = 0 
for i in levels:
    if i == 1: 
        if K== 0:
            show_start_screen()
            fase1 ()
            
            if K == 1:
                # prox_nivel()
                fase2()
                # igual fase 1 so que maia rapido

                if K == 2: 
                    # prox_nivel()
                    fase3()
                    # igual fase 2 so que mais rapido 

                    if K == 3:
                        salvou_reino()
                        #tela de voce ganhou 