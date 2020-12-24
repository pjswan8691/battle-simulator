import random, time, math

types = {
    "fire" : 0,
    "water" : 1,
    "grass" : 2
}

typeEffectivenessMatchup = [
      #Fire  #Water #Grass
    [.5,    .5,     2],   #Fire
    [ 2,    .5,    .5],   #Water
    [.5,     2,    .5]    #Grass
]

class Move():
    def __init__(self, moveName, basePower, moveType, special):
        self.moveName = moveName
        self.basePower = basePower
        self.moveType = moveType
        self.special = special

""" Physical Moves """
PH_fireLash = Move("Fire Lash", 65, "fire", False)
PH_flipTurn = Move("Flip Turn", 60, "water", False)
PH_grassySlide = Move("Grassy Slide", 70, "grass", False)

""" Special Moves """
SP_burnUp = Move("Burn Up", 130, "fire", True)
SP_hydroPump = Move("Hydro Pump", 110, "water", True)
SP_petalDance = Move("Petal Dance", 120, "grass", True)

movesList = {
    # Physical Moves
    "Fire Lash" : PH_fireLash,
    "Flip Turn" : PH_flipTurn,
    "Grassy Slide" : PH_grassySlide,
    # Special Moves
    "Burn Up" : SP_burnUp,
    "Hydro Pump" : SP_hydroPump,
    "Petal Dance" : SP_petalDance
}

class GeneratePokemon():
    def __init__(self, name, health, level, pokType, attack, defense, speed, learnset):
        self.name = name
        self.health = health
        self.level = level
        self.pokType = pokType
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.learnset = learnset

    def ReceiveDamage(self, damage):
        self.health -= damage
        if(self.health <= 0):
            print(self.name," has fainted!")

    def Attack(self, move, target):
        target.ReceiveDamage(damageFx(self.level, movesList[move].basePower, self.attack, target.defense, move, target.pokType))

def damageFx(level, power, attack, defense, typeSelf, typeTarget):
    """
    
    Returns an float: damage calculated using the pokemon damage formula

    """
    effectiveness = typeEffectivenessMatchup[types[movesList[typeSelf].moveType]][types[typeTarget]]
               # Critical                                     # Random                   # STAB (Same type attack bonus)          # Type effectiveness
    modifier = (1.5 if random.randrange(1,16) == 16 else 1) * random.uniform(0.85,1.0) * (1.5 if typeSelf == typeTarget else 1) * (effectiveness)

    if effectiveness == .5:
        print("It's not very effective...")
    elif effectiveness == 2:
        print("It's super effective!")

    return ((((((level*2)/5)+2)*power*(attack/defense))/50)+2) * modifier

def GetWinner():
    if(playerPok.health <= 0):
        print(enemyPok.name," has won the battle")
    else:
        print(playerPok.name," has won the battle")

# Pokemon setup
oppClass = input('Opponent: ')
playerClass = input('Player: ')

# Pokemon type selection
print('\n Select a pokemon type from the list:')
for typ in types.keys():
    print(typ)
typeSelected = input('Type: ')
while typeSelected not in types.keys():
    print('No type called',typeSelected)
    typeSelected = input('Type: ')

MaxMoveAmount = 4
# Moveset move amount selection
print('\n How many moves would you like to add? Max.',MaxMoveAmount,' Min. 1')
moveAmount = int(input('Amount: '))
while moveAmount > MaxMoveAmount or moveAmount < 1:
    print('Amount of moves should be between 1 and ',maxMoveAmount)
    moveAmount = int(input('Amount: '))

# Moveset selection
selectedLearnset = []
selectedAmount = 0
print('\n Select ',moveAmount,' moves from the list:')
for move in movesList:
    if movesList[move].special:
        print(move,' : special')
    else:
        print(move,' : physical')
while selectedAmount < moveAmount:
    selectedMove = input("Add Move: ")
    while selectedMove not in movesList:
        print('No move called ',selectedMove)
        selectedMove = input('Physical move: ')
    selectedAmount += 1
    selectedLearnset.append(selectedMove)

enemyLearnSet = [
    "Fire Lash",
    "Burn Up"
]

enemyPok = GeneratePokemon(oppClass, 1000, 99, "fire", 100, 100, 10, enemyLearnSet)
playerPok = GeneratePokemon(playerClass, 1000, 99, typeSelected, 100, 100, 10, selectedLearnset)

def main():

    print("\n\n\n\n",playerPok.name," VS ",enemyPok.name,"\n")

    while (enemyPok.health > 0 and playerPok.health > 0):

        print('Select move to use from the list:')
        for move in playerPok.learnset:
            print(move)
        moveToUse = input('Move: ')
        while moveToUse not in playerPok.learnset:
            print('No move called ',moveToUse," available")
            moveToUse = input('Move: ')

        playerturn = False

        if enemyPok.speed > playerPok.speed:
            playerturn = False
        elif playerPok.speed > enemyPok.speed:
            playerturn = True
        else:
            randTurn = random.randrange(0,1)
            if randTurn == 0:
                playerturn = True
            else:
                playerturn = False

        if playerturn:
            print(playerPok.name," uses ", moveToUse," against ",enemyPok.name)
            playerPok.Attack(moveToUse, enemyPok)
            print('\n')
            if(enemyPok.health > 0):
                print(enemyPok.name," uses ",enemyPok.learnset[random.randrange(0,len(enemyPok.learnset))]," against ",playerPok.name)
                enemyPok.Attack(enemyPok.learnset[random.randrange(0,len(enemyPok.learnset))], playerPok)
                print('\n')
        else:
            print(enemyPok.name," uses ",enemyPok.learnset[random.randrange(0,len(enemyPok.learnset))]," against ",playerPok.name)
            enemyPok.Attack(enemyPok.learnset[random.randrange(0,len(enemyPok.learnset))], playerPok)
            print('\n')
            if(playerPok.health > 0):
                print(playerPok.name," uses ", moveToUse," against ",enemyPok.name)
                playerPok.Attack(moveToUse, enemyPok)
                print('\n')
        
        print(playerPok.name,"| HP: ",round(playerPok.health))
        print(enemyPok.name,"| HP: ",round(enemyPok.health))
        print('\n')

    GetWinner()
    input('Press enter to continue . . .')
        

if __name__ == "__main__":
    main()
