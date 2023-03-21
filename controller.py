import pygame
import model

nomertimer=pygame.event.custom_type()
pygame.time.set_timer(nomertimer,1500)
nomertimer_2=pygame.event.custom_type()
pygame.time.set_timer(nomertimer_2,50)
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
        if s.type == nomertimer_2:
            model.sdvig_kyrs()

