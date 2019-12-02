#create a Spell class that inherits the attributes and behaviors of the Card class
#contructor or initiator that assigns the attributes of the class
#print statement 

#Spell has the attributes 
#name -- Card Class
#cost -- Card Class
#ability

from Card import Card

class Spell(Card):
    def __init__(self,cost,name,ability):
        Card.__init__(self,cost,name) #super()
        self.ability = ability
    #also inherits methods
    #no printCardInfo() method in Spell
    #overriding the method in Card
    def printCardInfo(self):
        print('The card cost: ' + str(self.cost))
        print('The card name: ' + self.name)
        print('Ability: '+ self.ability)

