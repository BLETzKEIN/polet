import pygame
import model

display = pygame.display.set_mode([model.WIDTH, model.HEIGHT])
bitcoi = pygame.image.load("kartinki/bitcoin.png")
bitcoin = pygame.transform.scale(bitcoi, model.rect_money.size)
elon_mas = pygame.image.load("kartinki/elon_mask.jpg")
elon_mask = pygame.transform.scale(elon_mas, model.rect.size)
balle = pygame.image.load("kartinki/img.png")
baller = pygame.transform.scale(balle, [250, model.HEIGHT])
kyr = pygame.image.load("kartinki/kyrs.png")
kyrs = pygame.transform.scale(kyr, [model.WIDTH, model.HEIGHT])

old_height = model.HEIGHT

kyrs_b=[350,400,100,600,500,550,200]

def weiv():
    global old_height, baller,kyrs
    if old_height != model.HEIGHT:
        baller = pygame.transform.scale(balle, [250, model.HEIGHT])
        kyrs = pygame.transform.scale(kyr, [model.WIDTH, model.HEIGHT])
        old_height = model.HEIGHT

    # display.fill([0, 0, 0])
    # pygame.draw.rect(display, [55, 98, 205], [model.WIDTH - 300, 0, 250, model.HEIGHT])
    # pygame.draw.rect(display, [90, 179, 202], model.rect_money)
    # pygame.draw.rect(display, [78, 190, 59], model.rect)
    display.blit(kyrs, [0, 0])
    display.blit(baller, [model.WIDTH - 300, 0])
    display.blit(bitcoin, model.rect_money)
    display.blit(elon_mask, model.rect)
    pygame.display.flip()
