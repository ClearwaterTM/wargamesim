import pygame, random, sys, modeles, optimisateur


def main():
    pygame.init()
    screen=pygame.display.set_mode((800,600))

    white=[255,255,255]
    darkRed = [128,0,0]
    fireBrick=[178,34,34]
    black=[0,0,0]

    screen.fill(darkRed)

    a = pygame.draw.rect(screen,fireBrick,(240,80,320,80))
    b = pygame.draw.rect(screen,fireBrick,(240,210,320,80))
    c = pygame.draw.rect(screen,fireBrick,(240,340,320,80))

    font_obj = pygame.font.Font('freesansbold.ttf', 28)

    text_surface_obj = font_obj.render('Simuler une bataille', True, white,fireBrick)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (400, 120)
    screen.blit(text_surface_obj, text_rect_obj)

    text_surface_obj1 = font_obj.render('Optimiser une armée', True, white,fireBrick)
    text_rect_obj1 = text_surface_obj1.get_rect()
    text_rect_obj1.center = (400, 250)
    screen.blit(text_surface_obj1, text_rect_obj1)

    text_surface_obj2 = font_obj.render('Quitter', True, white,fireBrick)
    text_rect_obj2 = text_surface_obj2.get_rect()
    text_rect_obj2.center = (400, 380)
    screen.blit(text_surface_obj2, text_rect_obj2)

    pygame.display.set_caption("Wargame")
    pygame.display.update()


    while True:

        mouselocation = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if text_rect_obj.collidepoint(mouselocation):
                        print("Démarrage du simulation.")
                        screen.fill((0,0,0))
                        pygame.display.update()
                        modeles.main(screen)
                    elif text_rect_obj1.collidepoint(mouselocation):
                        print("Début du optimisation.")
                        screen.fill((0,0,0))
                        optimisateur.main(screen)
                    elif text_rect_obj2.collidepoint(mouselocation):
                        print("Sortie du programme.")
                        sys.exit()

