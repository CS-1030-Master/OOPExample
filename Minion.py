# This class needs to inherit the attributes
# and behaviors of the Card class
# A Minion object is a Card
# Child Class -- derived class
from Card import Card

class Minion(Card):
    # attribute cost and name
    # inherits cost and name from the parent class Card
    def __init__(self, cost, name, damage, life):
        Card.__init__(self, cost, name)
        #assign parameters to the object
        self.damage = damage
        self.life = life
    
    #override method-ish
    def printMinionInfo(self):
        print('The card cost: ' + str(self.cost))
        print('The card name: ' + self.name)
        print('damage: ' + str(self.damage))
        print('life: '+ str(self.life))
    