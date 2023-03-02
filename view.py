import pygame
import model

display = pygame.display.set_mode([model.WIDTH, model.HEIGHT])


def weiv():
    display.fill([0, 0, 0])
    pygame.draw.rect(display, [55, 98, 205], [model.WIDTH - 300, 0, 250, model.HEIGHT])
    pygame.draw.rect(display, [90, 179, 202], model.rect_money)
    pygame.draw.rect(display, [78, 190, 59], model.rect)
    pygame.display.flip()
