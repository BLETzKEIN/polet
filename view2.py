import pygame
import model

display = pygame.display.get_surface()
old_height = model.HEIGHT

ca = pygame.image.load('kartinki/fon_menu.jpg')
cat = pygame.transform.scale(ca,[model.WIDTH,model.HEIGHT])

f = pygame.font.SysFont("arial", 30, True, False)

def weiv():
    global old_height,cat
    if old_height != model.HEIGHT:
        cat = pygame.transform.scale(ca,[model.WIDTH,model.HEIGHT])
        old_height = model.HEIGHT
    display.blit(cat,[0,0])

    q = f.render("нажмите ESC чтобы начать",True,[46,83,251],[0,0,0])
    display.blit(q,[0,0])
    record = f.render( "максимальный результат "+ str(model.speed_record),True,[46,83,251],[0,0,0])
    display.blit(record,[0,34])
    pygame.display.flip()