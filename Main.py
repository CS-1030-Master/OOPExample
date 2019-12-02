from Card import Card
from Spell import Spell
from Minion import Minion

def main():
    # create thexcx townCrier Card --object--
    # cost = 1 and name = 'Town Crier'
    # instantiate an object called townCrier
    # creating an instance of the class
    townCrier = Minion(1,'Town Crier', 1, 2)
    #create an instance of the class called redbandWasp
    #attributs cost = 2 and the name = Redband Wasp
    redbandWasp = Minion(2, 'Redband Wasp',1,3)
    warpath = Spell(2, 'Warpath', 'Deal 1 damage to all minions')
    #show the player the details of the card

    print('Town Crier Card')
    townCrier.printMinionInfo()
    print('\nRed Band Wasp Card')
    redbandWasp.printCardInfo()
    print('\nWarpath Card')
    warpath.printCardInfo()

if __name__=="__main__":
    main()