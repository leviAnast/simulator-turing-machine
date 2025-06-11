import pygame
import sys
from Machine import Machine
from interface import Interface
from leitura_arquivo import ler_arquivo  

pygame.init()
screen = pygame.display.set_mode((1000, 400))


file_path = "Entrada_AB.txt" #"Entrada_Palindromo.txt"  "Entrada_Contem0.txt"  "Entrada_Multiplo3.txt"  "Entrada_Par.txt"  "Entrada_AB.txt"

estado_inicial, fita = ler_arquivo(file_path)
mt = Machine(estado_inicial, fita, 30)

interface = Interface(screen, mt)
clock = pygame.time.Clock()

running = True

while running:
    interface.draw()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not mt.run():
                    interface.define_final_msn()
                    
    clock.tick(30)

pygame.quit()
sys.exit()
   