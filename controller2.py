import pygame
import model


def events():
    b = pygame.event.get()
    for s in b:
        if s.type == pygame.KEYDOWN:
            if s.key == pygame.K_ESCAPE:
                print(s)
                model.smena_sceni()