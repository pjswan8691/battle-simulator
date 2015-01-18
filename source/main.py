import random, time

currPlayerHitToken = True
currOpponentHitToken = True

class GenerateMonster():
    def __init__(self, name, health, gold, weapon, ac, *specials):
        self.name = name
        self.health = health
        self.gold = gold
        self.weapon = weapon
        self.ac = ac

def checkMissPlayer(defender):
	global currPlayerHitToken
	missChance = random.randrange(0, 25)

	if missChance <= defender:
		currPlayerHitToken = False
		return currPlayerHitToken
	else:
		currPlayerHitToken = True
		return currPlayerHitToken

def checkMissOpponent(defender):
	global currOpponentHitToken
	missChance = random.randrange(0, 25) # make this variable

	if missChance <= defender:
		currOpponentHitToken = False
		return currOpponentHitToken
	else:
		currPlayerHitToken = True
		return currOpponentHitToken

def determineDamage(weapon, modifier, directed): #(weapon, modifier, directed)
	if weapon == "fists" or weapon == "claws":
		return inflictDamage(player, 2 * modifier, 6 * modifier)
	elif weapon == "Iron Broadsword":
		return inflictDamage(opponent, 100, 250)
	return

def usePlayerSpecial(action):
	if attack == "Holy Light":
		#code
	elif attack == "Retribution":
		#code
	else:
		return 'error'

def inflictDamage(inflicted, min, max):
	damageInflicted = random.randrange(min, max+1)
	if damageInflicted == 0:
		return 'Miss!'
	else:
		inflicted.health-=damageInflicted
		return damageInflicted

def getWinner(player, enemy):
	if player.health > enemy.health:
		print player.name, 'wins!'
	else:
		print enemy.name, 'wins!'

def getHP(character):
	return character.health

opponent = GenerateMonster('Goblin King', 1000, 100, 'fists', 15, ['Shred'])
player = GenerateMonster('Paladin', 150, 200, 'Iron Broadsword', 15, ['Holy Light', 'Retribution'])

def main():

	playerInitialHealth = player.health
	opponentInitialHealth = opponent.health

	while (opponent.health >= 0) and (player.health >= 0):

		time.sleep(1)

		#print checkMissPlayer(opponent.ac)
		if (currPlayerHitToken):
			print "%s HP:" % player.name, getHP(player)
			print "Damage to %s:" % opponent.name, determineDamage(player.weapon, 1, opponent.health)
		else:
			print '%s HP:' % player.name, getHP(player)
	   		print '%s missed!' % player.name

		time.sleep(1)

	   	#print checkMissOpponent(player.ac)

	   	if(currOpponentHitToken):
	   		print "%s HP:" % opponent.name, getHP(opponent)
	   		print "Damage to: %s" % player.name, determineDamage(opponent.weapon, 1, player.health)
	   	else:
	   		print "%s HP:" % opponent.name, getHP(opponent)
	   		print '%s missed!' % opponent.name

	getWinner(player, opponent)

if __name__ == "__main__":
	main()
