import random


class army:
   
    #Constructeur
    def __init__(self):
        maxPoints = 250
       
        # Variable pour les types d'unités dans l'armée - chaque donée correspond a un objet de unité d'armée.
        # Taille maximum: 10 unités par armée.
        
        maxArmyUnits = 10
        
        #Ceci reste vide à l'initialisation - elle sera rempli/vidé à travers le jeu.

        armyUnits = []
        
class unit:
    def __init__(self):
        #Coordonées sur le plateau du jeu.
        location = [0,0]
        
        #L'unité a-t-elle deja été déplacée?
        alreadyMoved = False
        
        #L'unité est-elle morte?
        isDead = False
        
        #Quelle armée se trouve cet unité?
        belongsToArmy = 0
        
        #Nombre de blessures que cet unité porte.
        numberOfWounds = 0
        
        #Nombre de points que cet unité coute.
        pointCost = 10
        
    def __init__(self, Health, Wounds, Agility, Movement, Range, Cost, Name):
        self.Health = Health
        self.Wounds = Wounds
        self.Agility = Agility
        self.Movement = Movement
        self.Range = Range
        self.Cost = Cost
        self.name = Name




Archer = unit(3,0,9,1,5, 18,"Archer")
Chevalier = unit(6,0,9,1,1, 17,"Knight")


def temp():
    print("Archer:")
    print(Archer.Health," HP")
    print(Archer.Wounds," Wounds")
    print(Archer.Agility," Agility")
    print(Archer.Movement,"Movement")
    print(Archer.Range,"Range")
    print("Cost :" ,Archer.Cost,"gold\n")

    while Archer.Wounds < Archer.Health :
        Probability= random.randint(1,10)
        if Probability!=10:
            print("\n\nSuccess! Archer hitten\n")
            Archer.Wounds+=1
            print("Archer:")
            print(Archer.Health," HP")
            print(Archer.Wounds," Wounds\n")
        else:
            print("Attack failed!\n")

    if Archer.Wounds==Archer.Health:
        print("Archer is dead!")
