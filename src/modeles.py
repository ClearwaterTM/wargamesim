# Fichier original par Daniel MURRAY.
# Cet fichier sert à construire nos modèles d'objets pour le simulateur (unités, champ de bataille, etc...)

# Si vous voulez porter des modifications, faites les commandes suivantes dans votre ligne de commandes:
# svn checkout https://forge.info.unicaen.fr/svn/wargame-h-l-m-d --username=NUMEDUTIANT (pour copier le repositoire local vers votre ordi)
# svn update (pour vérifier que le repositoire est à jour)
# svn commit fichier -m message (pour mettre les modifications effectués dans le fichier en ligne)
# Example: svn commit modeles.py -m "Ceci est un commit de test"

#Importer les libraries necessaires pour notre projet.
import numpy
import random
import time
import os
import sys
import pygame
import main_menu

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Objective:
    def __init(self,x,y,currentControl):
        self.x = x
        self.y = y
        self.currentControl = currentControl

# Fonction pour calculer la distance entre deux points d'une grille avec la méthode "distance Manhattan".
def distanceBetweenTwoPoints(point1,point2):
    return (abs((point1.x - point2.x) + (point1.y - point2.y)))
    
def distanceBetweenTwoUnits(point1,point2):
    return (abs((point1[0] - point2[0]) + (point1[1] - point2[1])))

# Mettre le plateau du jeu sur l'interface graphique à jour.
def updateGraphicsGrid(screen,grid,gridCoordinates):
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

 
# Champ de bataille
class Battlefield:

    # Ajouter l'emplacement des objectifs dans le champ.
    def setUpObjectives(self):
    
        print("Generation de ", self.numOfObjectives,   " objectifs...")
        numOfObjectivesLeft = self.numOfObjectives
        seed = 0
        alreadyPlaced = 0

        while numOfObjectivesLeft > 0:
            print("running")
            for a in range(3,len(self.grid)-3):
                for b in range(len(self.grid[a])):
                    seed = random.randint(0,50)
                    if seed == 1:
                        if alreadyPlaced == 0:
                            if numOfObjectivesLeft > 0:
                                self.grid[a][b] = "X"
                                alreadyPlaced = 1
                                numOfObjectivesLeft = numOfObjectivesLeft - 1
                                b = len(self.grid[a])+1

                    alreadyPlaced = 0
                    seed = 0
        print("end")

    # Fonction pour génerer des obstacles sur le terrain.
    def putObstaclesInMap(self, n):
    
        #Declaration des variables nécessaires.
        numOfObstaclesLeft = n
        seed = 0
        alreadyPlaced = 0
        
        #Algorithme principale pour le terrain.
        #Le terrain est representé par le caractère suivant: *
        while numOfObstaclesLeft > 0:
            for a in range(len(self.grid)):
                for b in range(len(self.grid[a])):
                    seed = random.randint(0,3)
                    if seed == 1:
                        if alreadyPlaced == 0:
                            self.grid[a][b] = "*"
                            alreadyPlaced = 1
                            numOfObstaclesLeft = numOfObstaclesLeft - 1
                            b = len(self.grid[a])-1

                        alreadyPlaced = 0
                        seed = 0

        #Afficher la grille modifié pour visualiser les changements.
        #for s in self.grid:
            #print(*s)

    #Effacer les bordures du terrain.
    def clearSides(self):
        self.grid[0] = ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]
        self.grid[1] = ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]
        self.grid[2] = ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]
        self.grid[len(self.grid)-1] = ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]
        self.grid[len(self.grid)-2] = ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]
        self.grid[len(self.grid)-3] = ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]

    #Constructeur
    def __init__(self):

        # Notre grille de bataille sera representé par un array de 16x16.

        self.grid = [
                    ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],
                    ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],
                    ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],
                    ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],
                    ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],
                    ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],
                    ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],
                    ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],
                    ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],
                    ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],
                    ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],
                    ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],
                    ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],
                    ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],
                    ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],
                    ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],
                    ]
        
        
        self.gridCoordinates = [
        [32,32],[62,32],[92,32],[122,32],[152,32],[182,32],[212,32],[242,32],[272,32],[302,32],[332,32],[362,32],[392,32],[422,32],[452,32],[482,32],
        [32,62],[62,62],[92,62],[122,62],[152,62],[182,62],[212,62],[242,62],[272,62],[302,62],[332,62],[362,62],[392,62],[422,62],[452,62],[482,62],
        [32,92],[62,92],[92,92],[122,92],[152,92],[182,92],[212,92],[242,92],[272,92],[302,92],[332,92],[362,92],[392,92],[422,92],[452,92],[482,92],
        [32,122],[62,122],[92,122],[122,122],[152,122],[182,122],[212,122],[242,122],[272,122],[302,122],[332,122],[362,122],[392,122],[422,122],[452,122],[482,122],
        [32,152],[62,152],[92,152],[122,152],[152,152],[182,152],[212,152],[242,152],[272,152],[302,152],[332,152],[362,152],[392,152],[422,152],[452,152],[482,152],
        [32,182],[62,182],[92,182],[122,182],[152,182],[182,182],[212,182],[242,182],[272,182],[302,182],[332,182],[362,182],[392,182],[422,182],[452,182],[482,182],
        [32,212],[62,212],[92,212],[122,212],[152,212],[182,212],[212,212],[242,212],[272,212],[302,212],[332,212],[362,212],[392,212],[422,212],[452,212],[482,212],
        [32,242],[62,242],[92,242],[122,242],[152,242],[182,242],[212,242],[242,242],[272,242],[302,242],[332,242],[362,242],[392,242],[422,242],[452,242],[482,242],
        [32,272],[62,272],[92,272],[122,272],[152,272],[182,272],[212,272],[242,272],[272,272],[302,272],[332,272],[362,272],[392,272],[422,272],[452,272],[482,272],
        [32,302],[62,302],[92,302],[122,302],[152,302],[182,302],[212,302],[242,302],[272,302],[302,302],[332,302],[362,302],[392,302],[422,302],[452,302],[482,302],
        [32,332],[62,332],[92,332],[122,332],[152,332],[182,332],[212,332],[242,332],[272,332],[302,332],[332,332],[362,332],[392,332],[422,332],[452,332],[482,332],
        [32,362],[62,362],[92,362],[122,362],[152,362],[182,362],[212,362],[242,362],[272,362],[302,362],[332,362],[362,362],[392,362],[422,362],[452,362],[482,362],
        [32,392],[62,392],[92,392],[122,392],[152,392],[182,392],[212,392],[242,392],[272,392],[302,392],[332,392],[362,392],[392,392],[422,392],[452,392],[482,392],
        [32,422],[62,422],[92,422],[122,422],[152,422],[182,422],[212,422],[242,422],[272,422],[302,422],[332,422],[362,422],[392,422],[422,422],[452,422],[482,422],
        [32,452],[62,452],[92,452],[122,452],[152,452],[182,452],[212,452],[242,452],[272,452],[302,452],[332,452],[362,452],[392,452],[422,452],[452,452],[482,452],
        [32,482],[62,482],[92,482],[122,482],[152,482],[182,482],[212,482],[242,482],[272,482],[302,482],[332,482],[362,482],[392,482],[422,482],[452,482],[482,482]
        ]
        
        self.obstacles = random.randint(10,15)
        self.numOfObjectives = random.randint(1,3) + 2

        # Generation des obstacles sur le terrain.
        self.putObstaclesInMap(4)

        # Effacer les côtés du terrain.
        self.clearSides()

        # Generation des objectifs sur le terrain.
        self.setUpObjectives()

#Unité d'armée
class Unit:

    def __init__(self, Health, Wounds, Agility, Movement, Range, Cost,Name, Location, isDead,belongsToArmy):
        self.Health = Health
        self.Wounds = Wounds
        self.Agility = Agility
        self.Movement = Movement ##On utilisera uniquement en cas d'ajout de rush ou charge différentes en fonction des unités
        self.Range = Range
        self.Cost = Cost
        self.Name = Name
        self.Location = Location
        self.isDead = isDead
        self.belongsToArmy = belongsToArmy


# Armée
class Army:
    
    #Remplir l'armée avec des unités de base.
    
    def createArmy(self,armyNumber):
        self.armyUnits = []
        print("Creation des unités dans l'armée...")
        for a in range(0,self.maxArmyUnits):
            s = Unit(5,0,3,3,5,15,"name",(0,0),0,armyNumber)
            self.armyUnits.append(s)
    
    #Constructeur de classe.
    def __init__(self,armyNumber):
        maxPoints = 250
        
        # Variable pour les types d'unités dans l'armée - chaque donée correspond a un objet de unité d'armée.
        # Taille maximum: 10 unités par armée.
        self.maxArmyUnits = 5
        
        #Ceci reste vide à l'initialisation - elle sera rempli/vidé à travers le jeu.
        self.armyUnits = [] 

        #L'identifiant de notre armée.
        
        
        #Creer l'armée en remplissant notre liste avec des objets d'unités.
        self.createArmy(armyNumber)
        
    

# Notre système de jeu
class System:

    #Chercher et retourner une liste de tous les coords des objectifs sur le champ.
    def getObjectives(self):
        objectiveLocations = []
        for b in range(0,len(self.gameBattlefield.grid)):
            for c in range(0,len(self.gameBattlefield.grid[b])):
                if self.gameBattlefield.grid[c][b] == "X":
                    toAdd = [b,c,0]
                    objectiveLocations += [toAdd]
        return objectiveLocations


    #Faire afficher le plateau du jeu sur l'écran.
    def showGrid(self):
        print("++++++++++++++++")
        for i in self.gameBattlefield.grid:
            print(*i)


    #Faire déplacer un unité sur un endroit donnée sur la plateau du jeu.
    def moveUnit(self, armyUnit, tileToMoveTo,grid):
    

        # Stocker les cases temporairement.
        toMoveFrom = grid[armyUnit.location[0]][armyUnit.location[1]]
        print("Moving from ", armyUnit.location[0], armyUnit.location[1])
        grid[armyUnit.location[0]][armyUnit.location[1]] = "-"
        
        #Déplacer l'unite, et mettre ses coords à jour.
        grid[tileToMoveTo.x][tileToMoveTo.y] = armyUnit.belongsToArmy
        armyUnit.location = (tileToMoveTo.x,tileToMoveTo.y)
        

# Verifier si la case selectionné est dans la portée de l'unité.
    def checkIfCaseIsValid(self,currentPosition, selectedcase, movementoption, gamegrid):
    
        maxmovement = 0
        if movementoption == 0:
            maxmovement = 0
        elif movementoption == 1:
            maxmovement = 6
        elif movementoption == 2 or movementoption == 3:
            maxmovement = 12
    
        print("Current unit: X - ", currentPosition.x, " Y - ", currentPosition.y)
        print("To move to: X - ", selectedcase.x, " Y - ", selectedcase.y)
    
        if distanceBetweenTwoPoints(currentPosition, selectedcase) > maxmovement+1:
            print("Trop loin!")
            return 1
        else:
            return 0
            
    # Fonction pour trouver s'il y a des objectifs non controlés sur le plateau du jeu.
    # Retourne 0 s'il y en a pas, sinon, retourne une liste [x,y] des coordonées de l'objectif qui est le plus proche de l'unité.
    def findNonControlledObjectives(self,armyUnit):
        flag = 0
        currentObjectives = self.getObjectives()
        # for a in range(0, len(currentObjectives)):
            # if currentObjectives[a][2] == 0:
                # flag = 1
                # #Supprimer tous les objectifs deja controlés.
                # for a in range(0,len(currentObjectives)):
                    # if currentObjectives[a][2] == 0:
                        # print(currentObjectives)
                        # toremove = [currentObjectives[a][0],currentObjectives[a][1],currentObjectives[a][2]]
                        # print("removing ", toremove)
                        # currentObjectives.remove(toremove)
                
                #Retourner l'objectif le plus proche de l'unité.
        shortestDistance = 99
        pointInList = 0

        for a in range(0,len(currentObjectives)):
            if distanceBetweenTwoPoints(Point(currentObjectives[a][0],currentObjectives[a][1]),Point(armyUnit.location[0],armyUnit.location[1])) < shortestDistance:
                    shortestDistance = distanceBetweenTwoPoints(Point(currentObjectives[a][0],currentObjectives[a][1]),Point(armyUnit.location[0],armyUnit.location[1]))
                    pointInList = a
                    
            y = currentObjectives[pointInList][0]
            x = currentObjectives[pointInList][1]
        return [x,y]
        if flag == 0:
            print("Not found")
            return 0


    def getShootableEnemiesAfterAdvance(self,armyunit,enemySymbol,nearestObjective,grid):

        #D'abord, cherchons le distance maximum qu'on puisse avancer vers l'objectif.
        distance = distanceBetweenTwoPoints(Point(armyunit.location[0],armyunit.location[1]),Point(nearestObjective[0],nearestObjective[1]))
    
        print("Objective coords:",nearestObjective[0],nearestObjective[1])
        # Stocker les coords x et y de l'unité pour qu'on puisse y retourner plus tard.
        tempx = armyunit.location[0]
        tempy = armyunit.location[1]
    
        for a in range(0,6):
            if armyunit.location[0] > nearestObjective[0] and a != 6:
                armyunit.location = ((armyunit.location[0] - 1),armyunit.location[1])
                a = a + 1
            if armyunit.location[0] < nearestObjective[0] and a != 6:
                print(armyunit.location)
                armyunit.location = ((armyunit.location[0] + 1),armyunit.location[1])
                a = a + 1
            if armyunit.location[1] > nearestObjective[1] and a != 6:
                armyunit.location = (armyunit.location[0],(armyunit.location[1] - 1))
                a = a + 1
            if armyunit.location[1] < nearestObjective[1] and a != 6:
                armyunit.location = (armyunit.location[0],(armyunit.location[1] + 1))
                a = a + 1
        
        
        print("Verifying area around", armyunit.location[0], armyunit.location[1])
        
        #Verifiez dans un aire du portée de l'unité s'il y a un ennemi dans la proximité.
        enemyLocations = []
        xborderless = 0
        yborderless = 0
        xborderplus = 0
        yborderplus = 0
        
        #Faire de sorte que l'anaylse de zone ne sort pas du plateau.
        
        if armyunit.location[0] - 5 < 0:
            xborderless = 0
        else:
            xborderless = armyunit.location[0] - 5
        if armyunit.location[0] + 5 > 15:
            xborderplus = 15
        else:
            xborderless = armyunit.location[0] + 5
        if armyunit.location[1] - 5 < 0:
            yborderless = 0
        else:
            yborderless = armyunit.location[1] - 5
        if armyunit.location[1] + 5 > 15:
            yborderplus = 15
        else:
            yborderless = armyunit.location[1] + 5
        
        for b in range (xborderless, xborderplus):
            for c in range(yborderless, yborderplus):
                if grid[b][c] == enemySymbol:
                    enemyLocations += [b,c]
         
        #Remettre les coords de l'unité a son défaut.
        armyunit.location = (tempx,tempy)
        
        
        if len(enemyLocations) == 0:
            return 0
        else:
            return enemyLocations


    
    def rushTowardsEnemy(self,currentArmy,armyUnit,grid):
        #Fonction pour faire courir une unité vers l'ennemi le plus proche possible.
        
        #D'abord, cherchez les coords de tous les ennemis présents sur la grille.
        
        enemyPositions = []
        
        for a in range(0,len(grid)):
            for b in range(0,len(grid[a])):
                if grid[a][b] == 2:
                    enemyPositions += [[a,b]]
       
        #Ensuite, chercher l'ennemi le plus proche de l'unité.
        shortestDistance = 99
        for c in range(0,len(enemyPositions)):
            
            if distanceBetweenTwoUnits(enemyPositions[c],armyUnit.location) < shortestDistance:
                    shortestDistance = distanceBetweenTwoUnits(enemyPositions[c],armyUnit.location)
                    pointInList = c
                    
            nearesty = enemyPositions[pointInList][0]
            nearestx = enemyPositions[pointInList][1]
        print("Nearest enemy: ", [nearesty,nearestx])
        
        #Enfin, chercher la grille le plus loin qu'on puisse se déplacer.
        #Déplacement max de 12 cases (a déterminer)
        currentx = armyUnit.location[0]
        currenty = armyUnit.location[1]
        
        # A FAIRE: Mettre ceci dans une fonction à part
        for d in range(0,2):
            if currentx > nearestx and d != 6:
                currentx = currentx - 1
                d = d + 1
            if currentx < nearestx and d != 6:
                currentx = currentx + 1
                d = d + 1
            if currenty > nearesty and d != 6:
                currenty = currenty - 1
                d = d + 1
            if currenty < nearesty and d != 6:
                currenty = currenty + 1
                d = d + 1
                
                
        # Vérifier que la grille qu'on veut se déplacer est bien vide. Si non, regarder si les cases autour d'elles sont valides.
        # S'ils le sont, décaler l'unité vers la nouvelle case.
        print(self.gameBattlefield.grid[currentx][currenty])
        
        if self.gameBattlefield.grid[currentx][currenty] != "-":
            print("INVALID CASE. RECTIFYING.")
            if self.gameBattlefield.grid[currentx+1][currenty] == "-":
                currentx = currentx + 1
            elif self.gameBattlefield.grid[currentx][currenty+1] == "-":
                currenty = currenty + 1
        
            
        print("****Moving unit to: ",currentx,currenty)
        
        self.moveUnit(armyUnit,Point(currentx,currenty),self.gameBattlefield.grid)
        
        # COMBAT FUNCTION GOES HERE.
        # self.attackUnit(armyUnit,unitToAttack)
        pass
        
    def computeOptions(self,currentArmy,armyUnit, grid,armyIdent):
        # L'arbre SHOOTING de décision que l'ordinateur va utiliser pour décider son action.
        
        print("Coords. de l'unité: [", armyUnit.location[0], ",",armyUnit.location[1],"]")
        enemySymbol = " "
        
        #Step 1: Chercher des objectifs non controlés
        if not self.findNonControlledObjectives(armyUnit):
            print("Aucun objectif non controlé.")
            #Step 2: Regarder s'il y a des ennemis tirables après avoir avancé.
            if armyIdent == 1:
                enemySymbol == "2"
            elif armyIdent == 2:
                enemySymbol == "1"
            if self.getShootableEnemiesAfterAdvance(armyUnit,enemySymbol,self.findNonControlledObjectives(armyUnit),self.gameBattlefield.grid):
               #Si oui, avancez vers l'objectif et tirez sur un ennemi si possible.
                print("Ennemi trouvé à l'avance.")
                print("Action prise: avancer vers objectif")
                self.advanceTowardsObjective(grid)
            else:
                #Sinon, courir vers l'objectif.
                print("Ennemi trouvé à l'avance.")
                print("Action prise: charger vers objectif")
                system.rushTowardsObjective(grid)
        else:
            print("Objectif non controlé trouvé.")
            #Step 3: Regarder s'il y a des ennemis tirables après avoir avancé.
            if armyIdent == 1:
                enemySymbol == "2"
            elif armyIdent == 2:
                enemySymbol == 1
            if self.getShootableEnemiesAfterAdvance(armyUnit,enemySymbol,self.findNonControlledObjectives(armyUnit),self.gameBattlefield.grid):
                 #Si oui, avancez vers l'ennemi et tirez sur un ennemi si possible.
                 print("Ennemi trouvé à l'avance.")
                 print("Action prise: Avancer vers l'ennemi.")
                 self.advanceTowardsEnemy(grid)
            else:
                #Sinon, courir vers l'ennemi.
                print("Aucun ennemi trouvé a l'avance.")
                print("Action prise: charger l'ennemi.")
                print("Coords. de l'unité: [", armyUnit.location[0], ",",armyUnit.location[1],"]")
                self.rushTowardsEnemy(currentArmy,armyUnit,grid)
        
    

    def unitActionPrompt(self,army,armyunit,grid,armyIdent):
    
        self.computeOptions(army,armyunit,grid,armyIdent)


    #Fait joueur un test de qualité (lancer de dé)
    def qualityTest(self, armyUnit):
        result = random.randint(0,6) + armyUnit.numberOfWounds
        return result > 6
        
    #Rouler des dés au début du jeu pour déterminer quel armee se deploiera en premier.
    def rollOff(self):
        player1roll = random.randint(0,6)
        time.sleep(.666)
        player2roll = random.randint(0,6)
        
        print ("Armee 1: ", player1roll, " - Armee 2: ", player2roll)
        
        if player1roll == player2roll:
            print("Egalite. Relancement des dés.")
            return self.rollOff()
        elif player1roll > player2roll:
            return 1
        else:
            return 2
    
    
    #Deployer la 1ere armee.
    def deployArmy1(self,grid):
        a = 0
        sectionToPick = random.randint(0,2)
            
        #Commencer par chercher tous les objectifs et leurs coordonées dans la grille.
        objectiveLocations = []
        for b in range(0,len(grid)):
            for c in range(0,len(grid[a])):
                if grid[b][c] == "X":
                    toAdd = [b,c]
                    objectiveLocations += [toAdd]
            
            
        #Prendre tous les points qui se situent sur la ligne de deploiement.
        deploymentLineLocations = []
            
        for x in range(0,len(grid[sectionToPick])):
            toAdd = [sectionToPick,x]
            deploymentLineLocations += [toAdd]
            
        #Chercher l'objectif le plus proche du ligne de déploiement en comparant les coords y.
        shortestDistance = 99
        pointInList = 0
            
        for a in range(0,len(objectiveLocations)):
            if objectiveLocations[a][1] - sectionToPick < shortestDistance:
                shortestDistance = objectiveLocations[a][1] - sectionToPick
                pointInList = a
        y = objectiveLocations[pointInList][0]
        x = sectionToPick;
            
        startingx = x
        startingy = y    
            
        grid[x][y] = self.gameArmy1.armyUnits[0].belongsToArmy
        self.gameArmy1.armyUnits[0].location = (sectionToPick,objectiveLocations[pointInList][0])  
        #Deployer les unités sur le ligne de deploiement.
        for z in range(1,len(self.gameArmy1.armyUnits)):
            if (z + 1 < len(grid[startingx])):
                grid[x][z+1] = self.gameArmy1.armyUnits[0].belongsToArmy
                self.gameArmy1.armyUnits[z].location = (x,(z+1))
            else:
                x = x+1
                
        for a in range(0,len(self.gameArmy1.armyUnits)):
            print(self.gameArmy1.armyUnits[a].location)
            
        
    #Deployer la 2eme armee.
    def deployArmy2(self,grid):
        a = 0
        sectionToPick = random.randint(13,15)
            
        #Commencer par chercher tous les objectifs et leurs coordonées dans la grille.
        objectiveLocations = []
        for b in range(0,len(grid)):
            for c in range(0,len(grid[a])):
                if grid[b][c] == "X":
                    toAdd = [b,c]
                    objectiveLocations += [toAdd]
            
            
        #Prendre tous les points qui se situent sur la ligne de deploiement.
        deploymentLineLocations = []
            
        for x in range(0,len(grid[sectionToPick])):
            toAdd = [sectionToPick,x]
            deploymentLineLocations += [toAdd]
            
        #Chercher l'objectif le plus proche du ligne de déploiement en comparant les coords y.
        shortestDistance = 99
        pointInList = 0
            
        for a in range(0,len(objectiveLocations)):
            if objectiveLocations[a][1] - sectionToPick < shortestDistance:
                shortestDistance = objectiveLocations[a][1] - sectionToPick
                pointInList = a
        y = objectiveLocations[pointInList][0]
        x = sectionToPick;
            
        startingx = x
        startingy = y    
            
        grid[x][y] = self.gameArmy1.armyUnits[0].belongsToArmy
        self.gameArmy2.armyUnits[0].location = (sectionToPick, objectiveLocations[pointInList][0])
        #Deployer les unités sur le ligne de deploiement.
        for z in range(1,len(self.gameArmy2.armyUnits)):
            if (z + 1 < len(grid[startingx])):
                grid[x][z+1] = self.gameArmy2.armyUnits[0].belongsToArmy
                self.gameArmy2.armyUnits[z].location = (x, (z+1))
            else:
                x = x+1
    
    #Deployer nos armées.
    def deployArmies(self,grid):
    
        self.deployArmy1(grid)
        self.deployArmy2(grid)
        
        
        #Afficher la grille dans la console pour pouvoir le comparer à l'affichage graphique.
        self.showGrid()
        
    
    
    
    def chargeArmies(self):
        for a in range(0,len(self.gameArmy1.armyUnits)):
            self.moveUnit(self.gameArmy1.armyUnits[a], Point((self.gameArmy1.armyUnits[a].x+1),(self.gameArmy1.armyUnits[a].y)), self.gameBattlefield.grid)
        for b in range(0,len(self.gameArmy2.armyUnits)):
            print(self.gameArmy2.armyUnits[b].x, self.gameArmy2.armyUnits[b].y)
            self.moveUnit(self.gameArmy2.armyUnits[b], Point((self.gameArmy2.armyUnits[b].x-1), (self.gameArmy2.armyUnits[b].y)), self.gameBattlefield.grid)
        self.showGrid()
    
    def waitForInput(self,screen):
        while True:
            pygame.display.update()
            mouselocation = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    screen.fill([155,155,155], (20, 555, 650, 30))
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_SPACE]:
                        return
    
    # Commencer notre boucle de jeu.
    def beginGameLoop(self,screen):
        font_obj = pygame.font.Font('freesansbold.ttf', 20)
        print("Démarrage du boucle du jeu.")
        print("Decision du premier armee pour le deploiement...")
        beginningPlayer = self.rollOff()
        print("L'armée", beginningPlayer, "a gagné le roulement.")
        
        print("Deploiement des armees...")
        self.deployArmies(self.gameBattlefield.grid)
        updateGraphicsGrid(screen,self.gameBattlefield.grid,self.gameBattlefield.gridCoordinates)
        
        maxTurnLimit = 10
        currentTurn = 0
        
        
        # Le jeu se lance a partir d'ici.
        gameLoop = True
        while gameLoop == True:
            for a in range(1,3):
                print(a)
                if a == 1:
                    #Armée 1
                    print(" ++++++++ Tour du armée 1 ++++++++")
                    for b in range(0,len(self.gameArmy1.armyUnits)):
                        self.unitActionPrompt(self.gameArmy1, self.gameArmy1.armyUnits[b],self.gameBattlefield.grid,1)
                        updateGraphicsGrid(screen,self.gameBattlefield.grid,self.gameBattlefield.gridCoordinates)
                        time.sleep(.250)
                        pygame.event.get()
                elif a == 2:
                    print("++++++++ Tour du armée 2 +++++++++")
                    for b in range(0,len(self.gameArmy2.armyUnits)):
                       self.unitActionPrompt(self.gameArmy2, self.gameArmy2.armyUnits[b],self.gameBattlefield.grid,2)
                       updateGraphicsGrid(screen,self.gameBattlefield.grid,self.gameBattlefield.gridCoordinates)
                       time.sleep(.250)
                       pygame.event.get()
            currentTurn = currentTurn + 1
                
                       
        # A la fin de chaque tour, regarder s'il y a toujours des unités d'une armée sur le plateau du jeu.
        # Si une armée est entièrement effacé, terminer le jeu en cours.
    
            amountOfArmy1Units = 0
            amountOfArmy2Units = 0
        
            for a in range(0,len((self.gameBattlefield.grid))):
                for b in range(0,len((self.gameBattlefield.grid[a]))):
                    if self.gameBattlefield.grid[a][b] == 1:
                        amountOfArmy1Units = amountOfArmy1Units + 1
                    elif self.gameBattlefield.grid[a][b] == 2:
                        amountOfArmy2Units = amountOfArmy2Units + 1
                        
            print(amountOfArmy1Units, amountOfArmy2Units)
            
            if amountOfArmy1Units == 0:
                print("Plus d'unités de l'armée 1 sur la grille!")
                self.endGame(2,screen)
            elif amountOfArmy2Units == 0:
                print("Plus d'unités de l'armée 2 sur la grille!")
                self.endGame(1,screen)
            elif currentTurn == maxTurnLimit:
                print("Limit de tours atteint, fin de la combat.")
                self.endGame(0,screen)
                           
            else:            
                # Attendre un input d'utilisateur avant de continuer la boucle.
                self.showGrid()
                text_endRoundInputWait_obj = font_obj.render('Fin de tour. Appuyer sur espace pour jouer le prochain tour.', True, [255,255,255],[155,155,155])
                text_endRoundInputWait_rec = text_endRoundInputWait_obj.get_rect()
                text_endRoundInputWait_rec.center = (330,570)
                screen.blit(text_endRoundInputWait_obj,text_endRoundInputWait_rec)
                self.waitForInput(screen)


    def endGame(self,winningArmy,screen):
    
        font = pygame.font.Font('freesansbold.ttf', 22)
    
        #Fonction pour traiter un fin de jeu.
        if winningArmy == 2:
            text_endGameArmy2_obj = font.render('L\'armée 2 a remporté la victoire.', True, [255,255,255],[155,155,155])
            text_endGameArmy2_rec = text_endGameArmy2_obj.get_rect()
            text_endGameArmy2_rec.center = (330,530)
            screen.blit(text_endGameArmy2_obj,text_endGameArmy2_rec)
        
        elif winningArmy == 1:
            text_endGameArmy1_obj = font.render('L\'armée 1 a remporté la victoire.', True, [255,255,255],[155,155,155])
            text_endGameArmy1_rec = text_endGameArmy1_obj.get_rect()
            text_endGameArmy1_rec.center = (330,530)
            screen.blit(text_endGameArmy1_obj,text_endGameArmy1_rec)
            
        elif winningArmy == 0:
            text_endGameArmy0_obj = font.render('Limite de tours atteint. Match nul.', True, [255,255,255],[155,155,155])
            text_endGameArmy0_rec = text_endGameArmy0_obj.get_rect()
            text_endGameArmy0_rec.center = (330,530)
            screen.blit(text_endGameArmy0_obj,text_endGameArmy0_rec)
            
        
        text_endOfSim_obj = font.render('Fin de la simulation. Appuyer sur espace pour retourner au menu principal.', True, [255,255,255],[155,155,155])
        text_endOfSim_rec = text_endOfSim_obj.get_rect()
        text_endOfSim_rec.center = (400,570)
        screen.blit(text_endOfSim_obj,text_endOfSim_rec)
            
            
        self.waitForInput(screen)
        main_menu.main()



    #Constructeur
    def __init__(self,screen):
    
        font_obj = pygame.font.Font('freesansbold.ttf', 28)
        
        
        #Pour notre système de jeu, nous allons print des messages au terminal pour aider à faire du débuggage
        print("Initialisation du système de jeu: ")
        
        print(" - Création du champ de bataille..: ")
        
        # Afficher notre champ de bataille sur l'écran.
        self.gameBattlefield = Battlefield()
        for y in range(1,17):
            for x in range(1,17):
                rect = pygame.Rect(x*(29+1), y*(29+1), 29, 29)
                pygame.draw.rect(screen, (230,230,230), rect, 2)
        
        
        text_waitForStart_obj = font_obj.render('Appuyer sur espace pour lancer la simulation.', True, [255,255,255],[155,155,155])
        text_rect_obj = text_waitForStart_obj.get_rect()
        text_rect_obj.center = (400, 570)
        screen.blit(text_waitForStart_obj, text_rect_obj)
        
        
        
        print(" - Création des armées... ")
        self.gameArmy1 = Army(1)
        print(self.gameArmy1.armyUnits)
        self.gameArmy2 = Army(2)
        
        print("Affichage du plateau de depart: ")
        
        
        self.showGrid()
        
        # Afficher la grille de départ et la légende sur l'interface graphique.
        
        updateGraphicsGrid(screen,self.gameBattlefield.grid,self.gameBattlefield.gridCoordinates)
        
        rect_army1 = pygame.Rect(550,330,20,20)
        pygame.draw.rect(screen,[0,255,0],rect_army1,0)
        
        rect_army2 = pygame.Rect(550,370,20,20)
        pygame.draw.rect(screen,[0,0,255],rect_army2,0)
        
        # Afficher la légende.
        font_obj_legend = pygame.font.Font('freesansbold.ttf', 22)
        
        text_legend_army1 = font_obj_legend.render('Armée 1', True, [255,255,255],[155,155,155])
        text_legend_army1_rec = text_legend_army1.get_rect()
        text_legend_army1_rec.center = (640,340)
        screen.blit(text_legend_army1,text_legend_army1_rec)
        
        text_legend_army2 = font_obj_legend.render('Armée 2', True, [255,255,255],[155,155,155])
        text_legend_army2_rec = text_legend_army2.get_rect()
        text_legend_army2_rec.center = (640,380)
        screen.blit(text_legend_army2,text_legend_army2_rec)
        
        
        text_legend_obstacle = font_obj_legend.render('Obstacle', True, [255,255,255],[155,155,155])
        text_legend_obstacle_rec = text_legend_obstacle.get_rect()
        text_legend_obstacle_rec.center = (640,420)
        
        text_legend_objective = font_obj_legend.render('Objectif', True, [255,255,255],[155,155,155])
        text_legend_objective_rec = text_legend_objective.get_rect()
        text_legend_objective_rec.center = (640,460)
        
        screen.blit(text_legend_obstacle,text_legend_obstacle_rec)
        screen.blit(text_legend_objective,text_legend_objective_rec)
        
        
        rect_legend = pygame.Rect(550,410,20,20)
        pygame.draw.rect(screen,[0,0,0],rect_legend,0)
        
        rect_objective = pygame.Rect(550,450,20,20)
        pygame.draw.rect(screen,[255,0,0],rect_objective,0)
        
        
        # Ensuite, attends le top de départ pour pouvoir lancer la simulation.
        while True:
            pygame.display.update()
            mouselocation = pygame.mouse.get_pos()
            for event in pygame.event.get():
                print(mouselocation)
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_SPACE]:
                        screen.fill([155,155,155], (75, 555, 650, 30))
                        pygame.display.update()
                        self.beginGameLoop(screen)
        
            

def main(screen):
    print("Demarrage du jeu...")
    screen.fill((155,155,155))
    pygame.display.update()
    gameSystem = System(screen)

