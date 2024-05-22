import pygame
import random
import time

from inicio import*
from Fase1 import* 
from Fase2 import*
from Fase3 import*
from salvou_reino import*


levels = [1,2,3]


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
import pygame
import random
import time

from inicio import *
from Fase1 import * 
from Fase2 import *
from Fase3 import *
from salvou_reino import *

# Define the levels
levels = [1, 2, 3]

# Initialize K to 0 at the beginning
K = 0

# Game loop
while K < len(levels):
    # Start the appropriate level based on the value of K
    if levels[K] == 1:
        show_start_screen()
        K = fase1()
    elif levels[K] == 2:
        show_start_screen()  # You might want to have a start screen for each level
        K = fase2()
    elif levels[K] == 3:
        show_start_screen()  # You might want to have a start screen for each level
        K = fase3()

# Player completed all levels
salvou_reino()