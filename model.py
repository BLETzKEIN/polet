import random

import pygame


def rict_money():
    global rect_money
    rect_money = pygame.Rect(random.randint(WIDTH - 300, WIDTH - 100), random.randint(0, HEIGHT - 50), 50, 50)
def delete_kyrs():
    del kyrs_b[0]
    randomiys = random.randint(-20, 20)
    element = kyrs_b[len(kyrs_b) - 1]
    kyrs_b.append(element + randomiys)


def update():
    global speedy, rect_money, display
    display = pygame.display.get_surface()
    if rect.left >= WIDTH:
        rect.right = 0

    if rect.bottom > HEIGHT:
        rect.bottom = HEIGHT
        speedy = -1

    if rect.top < 0:
        rect.top = 0
        speedy = 1

    rect.centerx += speedx
    rect.centery += speedy


def display_full():
    global WIDTH, HEIGHT, rect_money
    if pygame.display.is_fullscreen():
        WIDTH = 1400
        HEIGHT = 700
        pygame.display.set_mode([WIDTH, HEIGHT])
        rict_money()
    else:
        pygame.display.set_mode([0, 0], pygame.FULLSCREEN)
        WIDTH = display.get_width()
        HEIGHT = display.get_height()
        rict_money()


speedy = 1
speedx = 1
WIDTH = 1400
HEIGHT = 700
rect = pygame.Rect(100, 100, 1280 / 3, 720 / 3)

kyrs_step = 2
kyrs_b = [300]
for f in range(WIDTH // kyrs_step):
    randomiys=random.randint(-20, 20)
    element=kyrs_b[len(kyrs_b)-1]
    kyrs_b.append(element+randomiys)

rict_money()
