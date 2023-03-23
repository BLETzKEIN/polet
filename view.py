import random

import pygame
import model

display = pygame.display.set_mode([model.WIDTH, model.HEIGHT])

bitcoi = pygame.image.load("kartinki/bitcoin.png")
bitcoin = pygame.transform.scale(bitcoi, model.rect_money.size)

elon_mas = pygame.image.load("kartinki/elon_mask.jpg")
elon_mask = pygame.transform.scale(elon_mas, model.rect.size)

balle = pygame.image.load("kartinki/img.png")
baller = pygame.transform.scale(balle, model.rect_baller.size)


old_height = model.HEIGHT


def line():
    x_line = 0
    y_line = 300
    for i in model.kyrs_b:
        pygame.draw.line(display, [0, 255, 0], [x_line, y_line], [x_line + model.kyrs_step, i], 3)
        x_line = x_line + model.kyrs_step
        y_line = i


def weiv():
    global old_height, baller, kyrs
    if old_height != model.HEIGHT:
        baller = pygame.transform.scale(balle, model.rect_baller.size)
        old_height = model.HEIGHT

    display.fill([0, 0, 0])
    line()
    display.blit(baller, model.rect_baller)
    # pygame.draw.rect(display,[255,255,255],model.rect_baller)
    display.blit(bitcoin, model.rect_money)
    display.blit(elon_mask, model.rect)
    pygame.display.flip()
