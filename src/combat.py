# Fichier original par Malaubier Leo.
# Cet fichier sert à la simulation d'un combat et l'optimisation d'armés.
#des insertions on eu lieux du fichier modeles pour pouvoir réalisé les déplacement et l'optimisation des armés.  
import random
from copy import deepcopy
import matplotlib.pyplot as plt
import numpy as np
from math import *
######################################################
class Army:
    #Constructeur
    def __init__(self):
        maxPoints = 250

        # Taille maximum: 10 unités par armée.
        maxArmyUnits = 10
        
        #Ceci reste vide à l'initialisation - elle sera rempli/vidé
        #       à travers le jeu.
        armyUnits = []
        



class Unit:
    def __init__(self, Health, Wounds, Agility, Movement, Range, Cost,Name, Location, isDead):
        self.Health = Health
        self.Wounds = Wounds
        self.Agility = Agility
        self.Movement = Movement ##On utilisera uniquement en cas d'ajout de rush ou charge différentes en fonction des unités
        self.Range = Range
        self.Cost = Cost
        self.Name = Name
        self.Location = Location
        self.isDead = isDead


def typeOfUnits():
    halberdier = Unit(6,0,10,1,3,20,"Halberdier",[0,0],False)
    archer = Unit(3,0,9,1,5, 18,"Archer",[0,0],False)
    assassin = Unit(4,0,10,1,3,18,"Assassin",[0,0],False)
    knight = Unit(6,0,9,2,1, 17,"Knight",[0,0],False)
    infantryman = Unit(4,0,10,1,1,16,"Infantryman",[0,0],False)    
    stonethrower = Unit(3,0,1,1,10,15,"Stone thrower",[0,0],False)    
    pawn = Unit(2,0,1,1,1,5,"Pawn",[0,0],False)
    l=[archer, knight, assassin, pawn, halberdier, knight, infantryman,stonethrower]
    return l



########################################################

def creatingArmies(liste):
    l=[]
    price=300
    #s représentant le prix de l'armée à chaque tour!
    s=0
    while s<=price:
        a=random.choice(liste)
        s=s+a.Cost
        l.append(a)
            
    return l

#def distance(a,b):
#   return calculedistance(a,b)
def moveUnit(armyUnit, tileToMoveTo,grid):
    

    #Stocker les cases temporairement.
    x = armyUnit.Location[0]
    y = armyUnit.Location[1]
    
    toMoveFrom = grid[x][y]
    grid[armyUnit.Location[0]][armyUnit.Location[1]] = "-"
        
    #Déplacer l'unite, et mettre ses coords à jour.
    grid[tileToMoveTo[0]][tileToMoveTo[1]] = 0
    armyUnit.Location = (random.randint(1,5),random.randint(1,5))
   
    
def distanceBetweenTwoPoints(point1,point2):
    return (abs((point1[0] - point2[0]) + (point1[1] - point2[1])))


#Deployer la 1ere armee.
def deployArmy1(grid,armyToDeploy):
    a = 0
    sectionToPick = random.randint(0,2)
            
    #Prendre tous les points qui se situent sur la ligne de deploiement.
    deploymentLineLocations = []
            
    for x in range(0,len(grid[sectionToPick])):
        toAdd = [sectionToPick,x]
        deploymentLineLocations += [toAdd]
            

    #Deployer les unités sur le ligne de deploiement.
    for z in range(1,len(armyToDeploy)):
        if (z + 1 < len(grid[sectionToPick])):
            grid[sectionToPick][z+1] = armyToDeploy[0].Name
            armyToDeploy[0].Location = (sectionToPick,(z+1))
        else:
            x = x+1
            
#Deployer la 2eme armee.
def deployArmy2(grid,armyToDeploy):
    a = 0
    sectionToPick = random.randint(13,15)
            
    #Prendre tous les points qui se situent sur la ligne de deploiement.
    deploymentLineLocations = []
            
    for x in range(0,len(grid[sectionToPick])):
        toAdd = [sectionToPick,x]
        deploymentLineLocations += [toAdd]
            

    #Deployer les unités sur le ligne de deploiement.
    for z in range(1,len(armyToDeploy)):
        if (z + 1 < len(grid[sectionToPick])):
            grid[sectionToPick][z+1] = armyToDeploy[0].Name
            armyToDeploy[0].Location = (sectionToPick,(z+1))
        else:
            x = x+1
        

def rushTowardsEnemy(currentArmy,armyUnit,grid):
        #Fonction pour faire courir une unité vers l'ennemi le plus proche possible.
       
        #Ensuite, chercher l'ennemi le plus proche de l'unité.
        nearesty = 6
        nearestx = 6
        
        #Enfin, chercher la grille le plus loin qu'on puisse se déplacer.
        #Déplacement max de 12 cases (a déterminer)
        currentx = armyUnit.Location[0]
        currenty = armyUnit.Location[1]
        
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
        
        if grid[currentx][currenty] != "-":
            if grid[currentx+1][currenty] == "-":
                currentx = currentx + 1
            elif grid[currentx][currenty+1] == "-":
                currenty = currenty + 1
        return (currentx,currenty)
def attack(armies,grid):

    k=0#un compteur
    deployArmy1(grid,armies[0])#déploiment des armées sur la carte (grid)
    deployArmy2(grid,armies[1])
    for i in range(len(armies[0])):
        if len(armies)==1:  #on vérifi si le nombre d'armé est différent de 1 pour continuer
            return armies
        if i >= len(armies[0]):#on arrète quand le i est supérieur au nombre d'élément de l'armée.
            break
        coordsToMoveTo = rushTowardsEnemy(armies[0],armies[0][i],grid)#déplacment
        moveUnit(armies[0][i],coordsToMoveTo,grid)

        for c in range(len(armies[1])):#on vérifie la porté de chacun pour voir qui peux touché l'énnemis en face.
            if armies[0][k].Range <= distanceBetweenTwoPoints(armies[0][k].Location,armies[1][c].Location): #on vérifie si la range est bonne
                Pro=armies[0][k].Agility    #calcule pour voir si l'armé touche si l'on attaque
                Probability=random.randint(Pro,12)
                if  Probability ==10:
                    armies[1][c].Wounds=armies[1][c].Wounds+1   #inflige des dégats
                    if armies[1][c].Wounds >= armies[1][c].Health: #si la vie de l'unité attaqué est de 0, elle meur donc on la suprime
                        del armies[1][c]
                if len(armies[1])<2:
                    del armies[1]
                k=k+1
                break
            
        ar=armies.pop(0) #on switch les armé
        armies.append(ar)

VargloablNombrearme=26 #variable en global pour être ré utilisé plus tard(calcul stat)
def tour(): #utilisé pour créé les armé
    armies=[]
    for x in range(VargloablNombrearme):
        armies.append(creatingArmies(typeOfUnits()))
    return armies


    
def boucle(a,b,grid):    #boncle pour faire les combat
    c=0         #on réinitialise le comteur a 0.
    armies=[]      #liste vide
    armies.append(a)    #on apprend les deux armées dans la liste vide.
    armies.append(b)
    while len(armies)!=1:   #tant que le nombre d'armée est différentes de 1. 
         #print a enlevé, c'est pour vérifier les étapes. 
        #print("armé1:",len(armies[0]),"armé2:",len(armies[1]))
        attack(armies,grid)  #on utilise la fonction fait de combat. 
        c=c+1       #On ajoute 1 au conteur. 
    if len(armies)==1:  #Si le nombre d'armée est =1
        if c%2==1:  #Test paire ou impaire pour savoir le quelle des deux armée a gagné. 
            armies.clear()
            return 2 #perdu
        else:
            armies.clear()
            return 1 #gagné
    if len(armies)==2:
        print("ERREUR") #témoins pour voir les étapes. 
 

def BestArmies(): #fonction qui permet de calculé quelle sont les deux meuilleur armées et les deux pires
    grid = [
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

    listeBase=tour()
    b=0
    d=0
    ar=deepcopy(listeBase)   #on fait une liste des armées 
    liste=[] #une liste vide 
    liste2=[]
    maxVictoir=0
    maxDef=0
    p=0
    VICT=[] #liste des victoir
    for i in range (len(ar)): #pour le nombre d'amées qu'il y a
        vic=0  
        Per=0                    #victoir =0
        for j in range (len(ar)): #pour le nombre d'amées qu'il y a
            if i==j:        #si l'armée i = l'armée j on passe 
                pass
            else:       #si les armées son différentes, on fait les combat 
               #print("ça commence armé1:",len(ar[i]),"ar:",len(ar[j]))
                b=boucle(ar[i],ar[j],grid)   #on fait le combat entre l'armée 1 et l'armé 2
                ar.clear()
                ar=deepcopy(listeBase)
                #print("liste de Base après clear ar",len(listeBase))
                #print("après append armé1:",len(ar[i]),"ar:",len(ar[j]))
                if b==1:        #quand la fonction boucle return 1, c'est que l'armé 1 sélectionné a gagné. 
                    vic=vic+1      #compteur de victoir +1
                if b==2:
                    Per=Per+1
                VICT.append(vic)
        if len(liste)<2:    #si il y a moins de 2 objet dans la liste on ajoutes des choses dans la liste. 
            liste.append(ar[i])
            
        else:
            if vic>=maxVictoir: #si le nombre de victoir est supérieur au pécédent 1er (on vas gardé les 2 meilleur armées) b= 2eme, d= 1er. 
                if vic>=d:  
                    maxVictoir=d
                    d=vic
                    if len(liste) == 1:
                        x1=liste.pop(0) #On prend le premier de la liste et on le stock. 
                    else:
                        x1=liste.pop(0)
                        x2=liste.pop(0)
                    liste.append(ar[i])#on prend l'armée qui vien de combatre (d'être testé)
                    liste.append(x1) #on ajoute le second
                else:
                    maxVictoir=vic
                    liste.pop(1)
                    liste.append(ar[i])
        if (len(liste2)<2 and len(liste)>=2):#même fonctionnement pour calculé la pire
            liste2.append(ar[i])
        elif (len(liste2)>=2):
            if Per>=maxDef:
                if Per>=p:
                    maxDef=p
                    if len(liste2) ==1:
                        D1=liste2.pop(0)
                    else:
                        D1=liste2.pop(0)
                        D2=liste2.pop(0)
                    liste2.append(ar[i])
                    liste2.append(D1)


    G=deepcopy(liste[0])
    return liste, liste2,VICT,listeBase,G

class Stat: #class de statistique (permet de faire des liste plus facile a utilisé)
    def __init__(self,vie,cout,agility,mouvement,portee):
        self.vie = vie
        self.cout =cout
        self.agility =agility
        self.mouvement= mouvement
        self.portee=portee
def StatTotal():
    Gagnant1=Stat(0,0,0,0,0)
    Gagnant2=Stat(0,0,0,0,0)
    Perdant1=Stat(0,0,0,0,0)
    Perdant2=Stat(0,0,0,0,0)
    l=[Gagnant1,Gagnant2,Perdant1,Perdant2]
    return l

class Compte:#class de statistique (permet de faire des liste plus facile a utilisé) ici pour compté le nombre de chaque unité dans les amrées
    def __init__(self,Halberdier,Archer,Assassin,Knight,Infantryman,Stonethrower,Pawn):
        self.Halberdier = Halberdier
        self.Archer = Archer
        self.Assassin = Assassin
        self.Knight = Knight
        self.Infantryman = Infantryman
        self.Stonethrower = Stonethrower
        self.Pawn = Pawn
def ComptTotal():
    Gagnant1=Compte(0,0,0,0,0,0,0)
    Gagnant2=Compte(0,0,0,0,0,0,0)
    Perdant1=Compte(0,0,0,0,0,0,0)
    Perdant2=Compte(0,0,0,0,0,0,0)
    l=[Gagnant1,Gagnant2,Perdant1,Perdant2]
    return l
def CalculStat():

    ListeGP=StatTotal()
    gagnant,perdant,VICT,listeBase,GAN=BestArmies()
 
    for V1 in range(len(perdant[0])-1): #calcule général de chaque élément du perdant 1
        ListeGP[2].vie=ListeGP[2].vie+perdant[0][V1].Health
        ListeGP[2].cout=ListeGP[2].cout+perdant[0][V1].Cost
        ListeGP[2].agility=ListeGP[2].agility+perdant[0][V1].Agility
        ListeGP[2].mouvement=ListeGP[2].mouvement+perdant[0][V1].Movement
        ListeGP[2].portee=ListeGP[2].portee+perdant[0][V1].Range

    for V2 in range(len(perdant[1])-1):#calcule général de chaque élément du perdant 2
        ListeGP[3].vie=ListeGP[3].vie+perdant[1][V2].Health
        ListeGP[3].cout=ListeGP[3].cout+perdant[1][V2].Cost
        ListeGP[3].agility=ListeGP[3].agility+perdant[1][V2].Agility
        ListeGP[3].mouvement=ListeGP[3].mouvement+perdant[1][V2].Movement
        ListeGP[3].portee=ListeGP[3].portee+perdant[1][V2].Range
    
 
    for V3 in range(len(gagnant[0])-1):#calcule général de chaque élément du gagnant 1
        ListeGP[0].vie=ListeGP[0].vie+gagnant[0][V3].Health
        ListeGP[0].cout=ListeGP[0].cout+gagnant[0][V3].Cost
        ListeGP[0].agility=ListeGP[0].agility+gagnant[0][V3-1].Agility
        ListeGP[0].mouvement=ListeGP[0].mouvement+gagnant[0][V3].Movement
        ListeGP[0].portee=ListeGP[0].portee+gagnant[0][V3].Range
    
    for V4 in range(len(gagnant[1])-1):#calcule général de chaque élément du gagnant 1
        ListeGP[1].vie=ListeGP[1].vie+gagnant[1][V4].Health
        ListeGP[1].cout=ListeGP[1].cout+gagnant[1][V4].Cost
        ListeGP[1].agility=ListeGP[1].agility+gagnant[1][V4].Agility
        ListeGP[1].mouvement=ListeGP[1].mouvement+gagnant[1][V4].Movement
        ListeGP[1].portee=ListeGP[1].portee+gagnant[1][V4].Range

    vieTOTAPER=ListeGP[2].vie+ListeGP[3].vie#vie totale des perdant
    vieTOTAGAN=ListeGP[0].vie+ListeGP[1].vie#vie totale gagnant
    couTOTAPER=ListeGP[2].cout+ListeGP[3].cout#coup totale perdant
    couTOTAGAN=ListeGP[0].cout+ListeGP[1].cout#coup totale gagnant
    mouveTOTAPER=ListeGP[2].mouvement+ListeGP[3].mouvement#mouvement totalte perdant
    mouveTOTAGAN=ListeGP[0].mouvement+ListeGP[1].mouvement#mouvement totale gagnant
    porteeTOTAPER=ListeGP[2].portee+ListeGP[3].portee#portée totale perdant
    porteeTOTAGAN=ListeGP[0].portee+ListeGP[1].portee#portée totale gagnant
    agiliteeTOTAPER=ListeGP[2].agility+ListeGP[3].agility#agilité totale perdant
    agiliteeTOTAGAN=ListeGP[0].agility+ListeGP[1].agility#agilité totale gagant

    vietotale=vieTOTAGAN+vieTOTAPER #calcule totaux 
    couttotale=couTOTAGAN+couTOTAPER
    mouvementtotale=mouveTOTAGAN+mouveTOTAPER
    porteetotal=porteeTOTAGAN+porteeTOTAPER
    agiliteetotale=agiliteeTOTAGAN+agiliteeTOTAPER

    PourCvie=abs((vieTOTAGAN-vieTOTAPER)/((vietotale)/4))   #calcule qui permet de trouvé des valeur proche de 1
    PourCcout=abs((couTOTAGAN-couTOTAPER)/((couttotale)/4))
    PourCmouve=abs((mouveTOTAGAN-mouveTOTAPER)/((mouvementtotale)/4))
    PourCporte=abs((porteeTOTAGAN-porteeTOTAPER)/((porteetotal)/4))
    PourCagilite=abs((agiliteeTOTAGAN-agiliteeTOTAPER)/((agiliteetotale)/4))
    #print(PourCvie,PourCcout,PourCmouve,PourCporte,PourCagilite)
    #if VargloablNombrearme<=8:
     #   if (PourCvie==0.0 or PourCmouve==0.0 or PourCporte==0.0 or PourCagilite==0.0):
     #       CalculStat()
    #print(ListeGP[0].vie,ListeGP[1].vie,ListeGP[2].vie,ListeGP[3].vie)

    ListePourcent=[PourCvie,PourCcout,PourCmouve,PourCporte,PourCagilite]
    UnitComp=ComptTotal()
    for a in range(2):#compte le nombre de chacun des élément des armés gagant
        for i in range(len(gagnant[a])):
            if gagnant[a][i].Name =="Halberdier":
                UnitComp[a].Halberdier=UnitComp[a].Halberdier+1
            if gagnant[a][i].Name=="Archer":
                UnitComp[a].Archer=UnitComp[a].Archer+1
            if gagnant[a][i].Name=="Assassin":
                UnitComp[a].Assassin=UnitComp[a].Assassin+1
            if gagnant[a][i].Name=="Knight":
                UnitComp[a].Knight=UnitComp[a].Knight+1
            if gagnant[a][i].Name=="Infantryman":
                UnitComp[a].Infantryman=UnitComp[a].Infantryman+1
            if gagnant[a][i].Name=="Stone thrower":
                UnitComp[a].Stonethrower=UnitComp[a].Stonethrower+1
            if gagnant[a][i].Name=="Pawn":
                UnitComp[a].Pawn=UnitComp[a].Pawn+1

    ListeNGagnant=[UnitComp[0].Halberdier,UnitComp[0].Archer,UnitComp[0].Assassin,UnitComp[0].Knight,UnitComp[0].Infantryman,UnitComp[0].Stonethrower,UnitComp[0].Pawn]
    ListeNGagnant2=[UnitComp[1].Halberdier,UnitComp[1].Archer,UnitComp[1].Assassin,UnitComp[1].Knight,UnitComp[1].Infantryman,UnitComp[1].Stonethrower,UnitComp[1].Pawn]
    for b in range(2):
        for j in range(len(perdant[b])):#compte le nombre de chacun des élément des armés perdant
            if perdant[b][j].Name =="Halberdier":
                UnitComp[b+2].Halberdier=UnitComp[b+2].Halberdier+1
            if perdant[b][j].Name=="Archer":
                UnitComp[b+2].Archer=UnitComp[b+2].Archer+1
            if perdant[b][j].Name=="Assassin":
                UnitComp[b+2].Assassin=UnitComp[b+2].Assassin+1
            if perdant[b][j].Name=="Knight":
                UnitComp[b+2].Knight=UnitComp[b+2].Knight+1
            if perdant[b][j].Name=="Infantryman":
                UnitComp[b+2].Infantryman=UnitComp[b+2].Infantryman+1
            if perdant[b][j].Name=="Stone thrower":
                UnitComp[b+2].Stonethrower=UnitComp[b+2].Stonethrower+1
            if perdant[b][j].Name=="Pawn":
                UnitComp[b+2].Pawn=UnitComp[b+2].Pawn+1

    ListeNPerdant=[UnitComp[2].Halberdier,UnitComp[2].Archer,UnitComp[2].Assassin,UnitComp[2].Knight,UnitComp[2].Infantryman,UnitComp[2].Stonethrower,UnitComp[2].Pawn]
    ListeNPerdant2=[UnitComp[3].Halberdier,UnitComp[3].Archer,UnitComp[3].Assassin,UnitComp[3].Knight,UnitComp[3].Infantryman,UnitComp[3].Stonethrower,UnitComp[3].Pawn]
    A=0
    A2=0 #on trouve quelle est le nombre maximal de victoir dans la liste de victoir qu'il y a eu dans les combats
    for i in range (len(VICT)):#
        if VICT[i]>A:
            A=VICT[i]
            position=i 

    for i in range (len(VICT)):

        if i== position:
            pass
        else:
            if VICT[i]>A2:
                A2=VICT[i]
    print(A)
    return gagnant, perdant, ListePourcent, ListeNGagnant, ListeNGagnant2, ListeNPerdant,ListeNPerdant2,ListeGP,listeBase,A,GAN



def optimisation():
    grid = [
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

    ListeMembre=typeOfUnits()
    gagnant,perdant,ListePourcent,ListeNGagnant,ListeNGagnant2,ListeNPerdant,ListeNperdant2,ListeGP,listeBase,A,GAN=CalculStat()
    print(ListePourcent)
    StatAmelio=0
    StatAmelio2=0
    compt=0
    #on regarde quelle statistique sont les plus proche de 1(les plus élevé) pour détermier quelle est la statistique qui a cresé l'écart entre les gagnant et les perdant
    for i in range (len(ListePourcent)):
        if ListePourcent[i]>StatAmelio:
            StatAmelio=ListePourcent[i]
            position=i 

    for i in range (len(ListePourcent)):

        if i== position:
            pass
        else:
            if ListePourcent[i]>StatAmelio2:
                StatAmelio2=ListePourcent[i]
                compt=i
    print(position,StatAmelio,compt,StatAmelio2)
    placement=[position,compt]
    
    for i in range (1): #On met 1pour le moment, ce qui peux ammené a une amélioration pour faire plus de modification si l'on le veux
        if placement[0]==1:
            i=i+1
            if placement[i]==0:#vie
                for j in range(len(gagnant[0])):
                    if gagnant[0][j].Health<=3:
                        Comptetotal=0
                        if gagnant[0][j].Name=="Archer":
                            for b in range (len(ListeNGagnant)):
                                Comptetotal=Comptetotal+ListeNGagnant[b]
                            if (ceil((Comptetotal)*(1/5)))<=ListeNGagnant[1]:#esque le nombre d'archer est significatif? (devien significatif a partire de 4) fait car le passage d'une unité distance a corps a corps
                                pass
                            else:
                                for a in range (len(gagnant[0])):
                                    if gagnant[0][a].Name=="Archer":
                                        gagnant[0][a]=ListeMembre[4]
                                ListeNGagnant[1]=0               
                        Comptetotal=0
                        if gagnant[0][j].Name=="Stone thrower":
                            for b in range (len(ListeNGagnant)):
                                Comptetotal=Comptetotal+ListeNGagnant[b]
                            if (ceil((Comptetotal)*(1/5)))<=ListeNGagnant[5]:#esque le nombre de lancer de pierre est significatif? (devien significatif a partire de 4 s'il y a 20 unité par exemple)
                                pass
                            else:
                                for a in range (len(gagnant[0])):
                                    if gagnant[0][a].Name=="Stone thrower":
                                        gagnant[0][a]=ListeMembre[4]
                                ListeNGagnant[5]=0    
                        if (gagnant[0][j].Name)=="Pawn":
                            gagnant[0][j]=ListeMembre[1]

            if placement[i]==1:#cout
                pass
            if placement[i]==2:#move 
                for j in range(len(gagnant[0])):#même principes pour tout les autre calcules
                    if gagnant[0][j].Health<=3:
                        Comptetotal=0
                        if gagnant[0][j].Name=="Archer":
                            for b in range (len(ListeNGagnant)):
                                Comptetotal=Comptetotal+ListeNGagnant[b]
                            if (ceil((Comptetotal)*(1/5)))<=ListeNGagnant[1]:
                                pass
                            else:
                                for a in range (len(gagnant[0])):
                                    if gagnant[0][a].Name=="Archer":
                                        gagnant[0][a]=ListeMembre[1]   
                                ListeNGagnant[1]=0           
                        Comptetotal=0
                        if gagnant[0][j].Name=="Stone thrower":
                            for b in range (len(ListeNGagnant)):
                                Comptetotal=Comptetotal+ListeNGagnant[b]
                            if (ceil((Comptetotal)*(1/5)))<=ListeNGagnant[5]:
                                pass
                            else:
                                for a in range (len(gagnant[0])):
                                    if gagnant[0][a].Name=="Stone thrower":
                                        gagnant[0][a]=ListeMembre[1]
                                ListeNGagnant[5]=0   
                        if (gagnant[0][j].Name)=="Pawn":
                            Comptetotal=0
                            if (ceil((Comptetotal)*(1/5)))<=ListeNGagnant[1]:
                                for a in range (len(gagnant[0])):
                                    if (gagnant[0][j].Name)=="Pawn":
                                        gagnant[0][j]=ListeMembre[0]
                                        ListeNGagnant[5]=ListeNGagnant[1]+1 
                            Comptetotal=0
                            if (ceil((Comptetotal)*(1/5)))<=ListeNGagnant[5]:
                                for a in range (len(gagnant[0])):
                                    if (gagnant[0][j].Name)=="Pawn":
                                        gagnant[0][j]=ListeMembre[7]
                                        ListeNGagnant[5]=ListeNGagnant[5]+1   

            if placement[i]==3:#range
                for j in range(len(gagnant[0])):
                    if gagnant[0][j].Range<3: #tout ce qui a une range inférieur a 3 peux être remplacé, soit par quelque chose qui est équivalent en vie, soit par un arché ou in lanceur de pierre
                    
                        if gagnant[0][j].Name=="Assassin": #on remplace tous les assassin par des albardier car de base il on 4 de vie, 
                            for a in range (len(gagnant[0])):
                                if gagnant[0][a].Name=="Assassin":
                                    Comptetotal=0
                                    for a in range (len(ListeNGagnant)):
                                        Comptetotal=Comptetotal+ListeNGagnant[a]
                                    if(ceil((Comptetotal)*(1/5)))<=ListeNGagnant[2]:
                                        pass
                                    else:
                                        for a in range (len(gagnant[0])):
                                            if gagnant[0][a].Name=="Assassin":
                                                gagnant[0][a]=ListeMembre[4]
                                        ListeNGagnant[2]=0            
                    
                        if gagnant[0][j].Name=="Infantryman":#pareil
                            for b in range (len(gagnant[0])):
                                Comptetotal=0
                                if gagnant[0][b].Name=="Infantryman":
                                    for a in range (len(ListeNGagnant)):
                                        Comptetotal=Comptetotal+ListeNGagnant[a]
                                    if(ceil((Comptetotal)*(1/5)))<=ListeNGagnant[4]:
                                        pass
                                    else:
                                        for a in range (len(gagnant[0])):
                                            if gagnant[0][a].Name=="Infantryman":
                                                gagnant[0][b]=ListeMembre[4]


                    
                        if gagnant[0][j].Name=="Pawn":    #les pion faible en point de vie devienne des arché 
                            gagnant[0][j]=ListeMembre[0]
                    
            
            if placement[i]==4:#agility ici, on veux amélioré l'agilité, donc pour les unité a distance, on veux les meilleur en distance/ agilité, et au corp a corp, les meilleur en point de vie, agilité
                for j in range(len(gagnant[0])):
                    if gagnant[0][j].Agility<7: 
                        if (gagnant[0][j].Name)=="Pawn":    
                            for b in range (len(gagnant[0])):
                                if gagnant[0][b].Name=="Pawn":
                                    gagnant[0][b]=ListeMembre[0]

                        if (gagnant[0][j].Name)=="Stone thrower":    
                            for b in range (len(gagnant[0])):
                                if gagnant[0][b].Name=="Stone thrower":
                                    gagnant[0][b]=ListeMembre[0]
        else:
            if placement[i]==0:#vie
                for j in range(len(gagnant[0])):
                    if gagnant[0][j].Health<=3:
                        Comptetotal=0
                        if gagnant[0][j].Name=="Archer":
                            for b in range (len(ListeNGagnant)):
                                Comptetotal=Comptetotal+ListeNGagnant[b]
                            if (ceil((Comptetotal)*(1/5)))<=ListeNGagnant[1]:#esque le nombre d'archer est significatif? (devien significatif a partire de 4) fait car le passage d'une unité distance a corps a corps
                                pass
                            else:
                                for a in range (len(gagnant[0])):
                                    if gagnant[0][a].Name=="Archer":
                                        gagnant[0][a]=ListeMembre[4]
                                ListeNGagnant[1]=0               
                        Comptetotal=0
                        if gagnant[0][j].Name=="Stone thrower":
                            for b in range (len(ListeNGagnant)):
                                Comptetotal=Comptetotal+ListeNGagnant[b]
                            if (ceil((Comptetotal)*(1/5)))<=ListeNGagnant[5]:#esque le nombre de lancer de pierre est significatif? (devien significatif a partire de 4 s'il y a 20 unité par exemple)
                                pass
                            else:
                                for a in range (len(gagnant[0])):
                                    if gagnant[0][a].Name=="Stone thrower":
                                        gagnant[0][a]=ListeMembre[4]
                                ListeNGagnant[5]=0    
                        if (gagnant[0][j].Name)=="Pawn":
                            gagnant[0][j]=ListeMembre[1]

            if placement[i]==1:#cout
                pass
            if placement[i]==2:#move 
                for j in range(len(gagnant[0])):#même principes pour tout les autre calcules
                    if gagnant[0][j].Health<=3:
                        Comptetotal=0
                        if gagnant[0][j].Name=="Archer":
                            for b in range (len(ListeNGagnant)):
                                Comptetotal=Comptetotal+ListeNGagnant[b]
                            if (ceil((Comptetotal)*(1/5)))<=ListeNGagnant[1]:
                                pass
                            else:
                                for a in range (len(gagnant[0])):
                                    if gagnant[0][a].Name=="Archer":
                                        gagnant[0][a]=ListeMembre[1]   
                                ListeNGagnant[1]=0           
                        Comptetotal=0
                        if gagnant[0][j].Name=="Stone thrower":
                            for b in range (len(ListeNGagnant)):
                                Comptetotal=Comptetotal+ListeNGagnant[b]
                            if (ceil((Comptetotal)*(1/5)))<=ListeNGagnant[5]:
                                pass
                            else:
                                for a in range (len(gagnant[0])):
                                    if gagnant[0][a].Name=="Stone thrower":
                                        gagnant[0][a]=ListeMembre[1]
                                ListeNGagnant[5]=0   
                        if (gagnant[0][j].Name)=="Pawn":
                            Comptetotal=0
                            if (ceil((Comptetotal)*(1/5)))<=ListeNGagnant[1]:
                                for a in range (len(gagnant[0])):
                                    if (gagnant[0][j].Name)=="Pawn":
                                        gagnant[0][j]=ListeMembre[0]
                                        ListeNGagnant[5]=ListeNGagnant[1]+1 
                            Comptetotal=0
                            if (ceil((Comptetotal)*(1/5)))<=ListeNGagnant[5]:
                                for a in range (len(gagnant[0])):
                                    if (gagnant[0][j].Name)=="Pawn":
                                        gagnant[0][j]=ListeMembre[7]
                                        ListeNGagnant[5]=ListeNGagnant[5]+1   

            if placement[i]==3:#range
                for j in range(len(gagnant[0])):
                    if gagnant[0][j].Range<3: #tout ce qui a une range inférieur a 3 peux être remplacé, soit par quelque chose qui est équivalent en vie, soit par un arché ou in lanceur de pierre
                    
                        if gagnant[0][j].Name=="Assassin": #on remplace tous les assassin par des albardier car de base il on 4 de vie, 
                            for a in range (len(gagnant[0])):
                                if gagnant[0][a].Name=="Assassin":
                                    Comptetotal=0
                                    for a in range (len(ListeNGagnant)):
                                        Comptetotal=Comptetotal+ListeNGagnant[a]
                                    if(ceil((Comptetotal)*(1/5)))<=ListeNGagnant[2]:
                                        pass
                                    else:
                                        for a in range (len(gagnant[0])):
                                            if gagnant[0][a].Name=="Assassin":
                                                gagnant[0][a]=ListeMembre[4]
                                        ListeNGagnant[2]=0            
                    
                        if gagnant[0][j].Name=="Infantryman":#pareil
                            for b in range (len(gagnant[0])):
                                Comptetotal=0
                                if gagnant[0][b].Name=="Infantryman":
                                    for a in range (len(ListeNGagnant)):
                                        Comptetotal=Comptetotal+ListeNGagnant[a]
                                    if(ceil((Comptetotal)*(1/5)))<=ListeNGagnant[4]:
                                        pass
                                    else:
                                        for a in range (len(gagnant[0])):
                                            if gagnant[0][a].Name=="Infantryman":
                                                gagnant[0][b]=ListeMembre[4]


                    
                        if gagnant[0][j].Name=="Pawn":    #les pion faible en point de vie devienne des arché 
                            gagnant[0][j]=ListeMembre[0]
                    
            
            if placement[i]==4:#agility ici, on veux amélioré l'agilité, donc pour les unité a distance, on veux les meilleur en distance/ agilité, et au corp a corp, les meilleur en point de vie, agilité
                for j in range(len(gagnant[0])):
                    if gagnant[0][j].Agility<7: 
                        if (gagnant[0][j].Name)=="Pawn":    
                            for b in range (len(gagnant[0])):
                                if gagnant[0][b].Name=="Pawn":
                                    gagnant[0][b]=ListeMembre[0]

                        if (gagnant[0][j].Name)=="Stone thrower":    
                            for b in range (len(gagnant[0])):
                                if gagnant[0][b].Name=="Stone thrower":
                                    gagnant[0][b]=ListeMembre[0]
    if placement[0]==0:#vie
        ChoixA="vie"
    if placement[0]==1:#cout
        if placement[1]==0:#vie   
            ChoixA="vie"         
        if placement[1]==2:#move
            ChoixA="déplacement" 
        if placement[1]==3:#range
            ChoixA="Portée"
        if placement[1]==4:#agility
            ChoixA="agilitée"
    if placement[0]==2:#move 
        ChoixA="déplacement" 
    if placement[0]==3:#range
        ChoixA="Portée"
    if placement[0]==4:#agility
        ChoixA="agilitée"

    ListeGP[1].vie=0
    ListeGP[1].cout=0
    ListeGP[1].agility=0
    ListeGP[1].mouvement=0
    ListeGP[1].portee=0
    for V1 in range(len(gagnant[0])-1): #calcule général de chaque élément du perdant 1
        ListeGP[1].vie=ListeGP[1].vie+gagnant[0][V1].Health
        ListeGP[1].cout=ListeGP[1].cout+gagnant[0][V1].Cost
        ListeGP[1].agility=ListeGP[1].agility+gagnant[0][V1].Agility
        ListeGP[1].mouvement=ListeGP[1].mouvement+gagnant[0][V1].Movement
        ListeGP[1].portee=ListeGP[1].portee+gagnant[0][V1].Range
    print(ListeGP[0].vie,ListeGP[0].cout,ListeGP[0].agility,ListeGP[0].mouvement,ListeGP[0].portee,"-----",ListeGP[1].vie,ListeGP[1].cout,ListeGP[1].agility,ListeGP[1].mouvement,ListeGP[1].portee)
    print("-------------------------------------")
    for i in range(len(gagnant[0])):
        print(gagnant[0][i].Name)
    print("-------------------------------------")
    for i in range(len(GAN)):
        print(GAN[i].Name)
    print("-------------------------------------")
    FINAL=gestionrapide(gagnant[0],perdant[0],grid)
    FI=gestionrapide(GAN,perdant[0],grid)
    print(FINAL,FI)
    POURCENFINAL=(100*FINAL)/20
    POURCENFI=(100*FI)/20
    if FINAL>FI:
        print("amélioration de", POURCENFINAL-POURCENFI,"% l'amélioration a donc marché")
        return gagnant[0],ChoixA,ListeGP[0],ListeGP[1]#la meilleur armé ListeGP[0]= gagant de base, ListeGP[1]= liste du gagnant amélioré
    if FI>FINAL:
        print("dégréssion de", POURCENFINAL-POURCENFI,"% l'amélioration n'a donc pas marché, pas de chance ")
        return GAN,ChoixA,ListeGP[0],ListeGP[1]#la meilleur armé
    if FINAL==FI:
        print("égalité")
        return gagnant[0],ChoixA,ListeGP[0],ListeGP[1]#l'une des deux meilleur armé



def gestionrapide(a,b,grid):
    G=deepcopy(a)
    G1=deepcopy(b)
    FINAL=0

    for i in range(20):
        G.clear()
        G1.clear()
        G=deepcopy(a)
        G1=deepcopy(b)
        RESU=boucle(G,G1,grid)
        if RESU==1:
            FINAL=FINAL+1
    return FINAL

def main():
    try:
        winningArmy = optimisation()
        return winningArmy[0]
    except UnboundLocalError:
        print("une erreur a eu lieu, on recommence")
        winningArmy = optimisation()
        return winningArmy[0]