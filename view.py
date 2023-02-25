import pygame
import model
display=pygame.display.set_mode([model.WIDTH,model.HEIGHT])
def weiv():
    display.fill([0,0,0])
    pygame.draw.rect(display,[78,190,59],model.rect)
    pygame.display.flip()