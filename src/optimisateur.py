# Cet fichier sert à notre optimisateur d'armée.

# Importer les fichiers nécessaires.
import numpy
import random
import time
import os
import sys
import pygame
import main_menu
import modeles
import combat

import matplotlib


# Notre système pour l'optimisateur.
class OptimizeSystem:
    
    def processResults(self,winningArmy,screen):
        font_optimisation = pygame.font.Font('freesansbold.ttf', 22)
        screen.fill([155,155,155])
       
        text_finished_obj = font_optimisation.render('Optimisation terminé. L\'armée le plus efficace pour le terrain est:', True, [255,255,255],[155,155,155])
        text_finished_rec = text_finished_obj.get_rect()
        text_finished_rec.center = (400,25)
        screen.blit(text_finished_obj,text_finished_rec)
                
        x = 350
        y = 70
        
        for a in range(0,len(winningArmy)):
            text_armyUnit_obj = font_optimisation.render(winningArmy[a].Name,True, [255,255,255],[155,155,155])
            text_armyUnit_rec = text_armyUnit_obj.get_rect()
            text_armyUnit_rec.center = (x,y)
            screen.blit(text_armyUnit_obj,text_armyUnit_rec)
            y = y + 25
            
            
        text_returnPrompt_obj = font_optimisation.render('Appuyer sur espace pour retourner au menu principale.', True, [255,255,255],[155,155,155])
        text_returnPrompt_rec = text_returnPrompt_obj.get_rect()
        text_returnPrompt_rec.center = (395,570)
        
        screen.blit(text_returnPrompt_obj,text_returnPrompt_rec)
        
        while True:
            pygame.display.update()
            mouselocation = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_SPACE]:
                        print("Début de l'optimisation...")
                        main_menu.main()
        


    def beginOptimisation(self,screen):
        font_optimisation = pygame.font.Font('freesansbold.ttf', 28)
        text_inProgress_obj = font_optimisation.render('Optimisation en cours. Veuillez patienter.', True, [255,255,255],[155,155,155])
        text_inProgress_rec = text_inProgress_obj.get_rect()
        text_inProgress_rec.center = (350,570)
        screen.blit(text_inProgress_obj,text_inProgress_rec)
        pygame.display.update()
       
        winningArmy = combat.main()
        print("Winning army is composed of the following:")
        for a in range(0,len(winningArmy)):
            print(winningArmy[a].Name)
        self.processResults(winningArmy,screen)



    # Mettre le plateau du jeu sur l'interface graphique à jour.
    def updateGraphicsGrid(self,screen,grid,gridCoordinates):
        counter = 0
        for a in range(0,len(grid)):
            for b in range(0,len(grid[a])):
                #Obstacle
                if grid[a][b] == "*":
                    rect = pygame.Rect(gridCoordinates[counter][0],gridCoordinates[counter][1],26,26)
                    pygame.draw.rect(screen,[0,0,0],rect)
                #Objectif
                elif grid[a][b] == "X":
                    rect = pygame.Rect(gridCoordinates[counter][0],gridCoordinates[counter][1],26,26)
                    pygame.draw.rect(screen,[255,0,0],rect)
                #Armée 1
                elif grid[a][b] == 1:
                    rect = pygame.Rect(gridCoordinates[counter][0],gridCoordinates[counter][1],26,26)
                    pygame.draw.rect(screen,[0,255,0],rect)
                #Armée 2
                elif grid[a][b] == 2:
                    rect = pygame.Rect(gridCoordinates[counter][0],gridCoordinates[counter][1],26,26)
                    pygame.draw.rect(screen,[0,0,255],rect)
                #Espace blanche
                elif grid[a][b] == "-":
                    rect = pygame.Rect(gridCoordinates[counter][0],gridCoordinates[counter][1],26,26)
                    pygame.draw.rect(screen,[155,155,155],rect)
                counter = counter + 1
        pygame.display.update()

    def __init__(self,screen):
        #D'abord, créez un plateau de jeu.
        proposedBattlefield = modeles.Battlefield()
        self.updateGraphicsGrid(screen,proposedBattlefield.grid, proposedBattlefield.gridCoordinates)
        
        #Ensuite, l'afficher sur l'écran.
        
        for y in range(1,17):
            for x in range(1,17):
                rect = pygame.Rect(x*(29+1), y*(29+1), 29, 29)
                pygame.draw.rect(screen, (230,230,230), rect, 2)
        
        
        font_obj = pygame.font.Font('freesansbold.ttf', 28)
        
        text_waitForStart_obj = font_obj.render('Appuyer sur espace pour lancer l\'optimisation.', True, [255,255,255],[155,155,155])
        text_rect_obj = text_waitForStart_obj.get_rect()
        text_rect_obj.center = (400, 540)
        screen.blit(text_waitForStart_obj, text_rect_obj)
        
        text_promptNewTerrain_obj = font_obj.render('Appuyer sur H pour générer un nouveau plateau de jeu.', True, [255,255,255],[155,155,155])
        text_promptNewTerrain_rec = text_waitForStart_obj.get_rect()
        text_promptNewTerrain_rec.center = (350, 570)
        screen.blit(text_promptNewTerrain_obj, text_promptNewTerrain_rec)
        
        pygame.display.update()
        
        while True:
            pygame.display.update()
            mouselocation = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_SPACE]:
                        screen.fill([155,155,155], (0, 510, 800, 100))
                        print("Début de l'optimisation...")
                        self.beginOptimisation(screen)
                    elif keys[pygame.K_h]:
                        del proposedBattlefield
                        proposedBattlefield = modeles.Battlefield()
                        self.updateGraphicsGrid(screen,proposedBattlefield.grid, proposedBattlefield.gridCoordinates)
                    
                    





# Notre fonction principal de notre fichier. Ceci est appelé quand le bouton correspondant au menu principale pour accèder
# au optimisateur est cliqué.
def main(screen):
    print("Demarrage de l'optimisateur...")
    screen.fill((155,155,155))
    pygame.display.update()
    System = OptimizeSystem(screen)