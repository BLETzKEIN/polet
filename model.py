import random

import pygame


def append_kyrs():
    element = kyrs_b[len(kyrs_b) - 1]
    randomiys = random.randint(-20, 20)
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
    global rect_money,monet_vsego,speedx,speedy
    x = random.randint(rect_baller.left, rect_baller.right - 50)
    y = random.randint(rect_baller.top, rect_baller.bottom - 50)
    rect_money = pygame.Rect(x, y, 50, 50)
    monet_vsego += 1
    if monet_vsego % 10 == 0:
        speedx += 1
        if 0<speedy:
            speedy += 1
        if 0>speedy :
            speedy += -1


def create_baller():
    global rect_baller
    rect_baller = pygame.Rect(WIDTH - 400, 0, 400, HEIGHT)

def smena_sceni():
    global scena
    if scena == "menu":
        scena = "game"
    else:
        scena = "menu"

def sobirai_money (xy):
    global bitcoins
    if rect_money.collidepoint(xy):
        bitcoins+=1
        # print("ХАРОШ")
        rict_money()
        return True
    return False
def this_is_Elon_Mask ():
    global bitcoins
    if rect.colliderect(rect_money):
        bitcoins-=1
        rict_money()



def update():
    global speedy, rect_money, display
    display = pygame.display.get_surface()


    rect.centerx += speedx
    rect.centery += speedy
    this_is_Elon_Mask()

    if rect.left >= WIDTH:
        rect.right = 0

    if rect.bottom > HEIGHT:
        rect.bottom = HEIGHT
        speedy = -speedy

    if rect.top < 0:
        rect.top = 0
        speedy = -speedy



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
monet_vsego = 0
scena = "menu"

rect = pygame.Rect(100, 100, 1280 / 3, 720 / 3)
rect_baller = None


kyrs_step = 2
kyrs_b = []

recreate_kyrs()
create_baller()
rict_money()
