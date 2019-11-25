from Card import Card
from Minion import Minion

def main():
    # create the townCrier Card --object--
    # cost = 1 and name = 'Town Crier'
    # instantiate an object called townCrier
    # creating an instance of the class
    townCrier = Minion(1,'Town Crier', 1, 2)
    

    #create an instance of the class called redbandWasp
    #attributs cost = 2 and the name = Redband Wasp
    redbandWasp = Minion(2, 'Redband Wasp',1,3)
    warpath = Card(2, 'Warpath')
    #show the player the details of the card

    townCrier.printCardInfo()
    townCrier.printMinionInfo()


    redbandWasp.printCardInfo()
    warpath.printCardInfo()

if __name__=="__main__":
    main()