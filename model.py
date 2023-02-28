import pygame
rect=pygame.Rect(100,100,200,300)
rect_money=pygame.Rect(0,0,50,50)
speedy=1
speedx=1
WIDTH=1400
HEIGHT=700
display=pygame.display.get_surface()

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
def display_full():
    global WIDTH,HEIGHT
    if pygame.display.is_fullscreen():
        WIDTH = 1400
        HEIGHT = 700
        pygame.display.set_mode([WIDTH, HEIGHT])
    else:
        pygame.display.set_mode([0, 0], pygame.FULLSCREEN)
        WIDTH = display.get_width()
        HEIGHT = display.get_height()

