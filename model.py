import random

import pygame


def append_kyrs():
    randomiys = random.randint(-20, 20)
    element = kyrs_b[len(kyrs_b) - 1]
    new_element = element + randomiys
    if new_element <= 0:
        new_element += 100
    if new_element >= HEIGHT:
        new_element -= 100
    kyrs_b.append(new_element)


def sdvig_kyrs():
    del kyrs_b[0]
    append_kyrs()


def recreate_kyrs():
    kyrs_b.clear()
    kyrs_b.append(HEIGHT // 2)
    for f in range(WIDTH // kyrs_step):
        append_kyrs()


def rict_money():
    global rect_money
    x = random.randint(rect_baller.left, rect_baller.right - 50)
    y = random.randint(rect_baller.top, rect_baller.bottom - 50)
    rect_money = pygame.Rect(x, y, 50, 50)


def create_baller():
    global rect_baller
    rect_baller = pygame.Rect(WIDTH - 400, 0, 400, HEIGHT)


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
    else:
        pygame.display.set_mode([0, 0], pygame.FULLSCREEN)
        WIDTH = display.get_width()
        HEIGHT = display.get_height()
    recreate_kyrs()
    create_baller()
    rict_money()


speedy = 1
speedx = 1
WIDTH = 1400
HEIGHT = 700
bitcoins = 0

rect = pygame.Rect(100, 100, 1280 / 3, 720 / 3)
rect_baller = None

kyrs_step = 2
kyrs_b = []

recreate_kyrs()
create_baller()
rict_money()
