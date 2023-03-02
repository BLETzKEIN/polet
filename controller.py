import pygame
import model

nomertimer=pygame.event.custom_type()
pygame.time.set_timer(nomertimer,1500)
def events():
    b = pygame.event.get()
    for s in b:
        if s.type == pygame.QUIT:
            exit(666)
        if s.type == pygame.KEYDOWN:
            if s.key == pygame.K_F11:
                model.display_full()
        if s.type == nomertimer:
            model.rict_money()
