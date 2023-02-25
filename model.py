import pygame
rect=pygame.Rect(100,100,200,300)
speedy=1
speedx=1
WIDTH=1400
HEIGHT=700

def update():
    global speedy
    if rect.left>=WIDTH:
        rect.right=0

    if rect.bottom>HEIGHT:
        rect.bottom=HEIGHT
        speedy=-1

    if rect.top<0:
        rect.top=0
        speedy=1

    rect.centerx+=speedx
    rect.centery+=speedy
