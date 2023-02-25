import pygame
import model
display=pygame.display.get_surface()
def events():
    b = pygame.event.get()
    for s in b:
        if s.type == pygame.QUIT:
            exit(666)
        if s.type == pygame.KEYDOWN:
            if s.key == pygame.K_F11:
                if pygame.display.is_fullscreen():
                    model.WIDTH = 1400
                    model.HEIGHT = 700
                    pygame.display.set_mode([model.WIDTH, model.HEIGHT])
                else:
                    pygame.display.set_mode([0, 0], pygame.FULLSCREEN)
                    model.WIDTH = display.get_width()
                    model.HEIGHT = display.get_height()
