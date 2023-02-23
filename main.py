import random
import time

import pygame
WIDTH=1400
HEIGHT=700
display=pygame.display.set_mode([WIDTH, HEIGHT])
rect=pygame.Rect(100,100,200,300)
speedy=1
speedx=1

while True:
    time.sleep(1/60)
    b=pygame.event.get()
    for s in b:
        if s.type==pygame.QUIT:
            exit(666)
    if rect.left>=WIDTH:
        rect.right=0


    rect.centerx+=speedx
    rect.centery+=speedy

    display.fill([0,0,0])
    pygame.draw.rect(display,[78,190,59],rect)
    pygame.display.flip()