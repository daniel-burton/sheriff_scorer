"""this program creates a "player score" object for each
player (from an interactive text prompt) and then gets the 
scores in each category for each player. It then calculates the
bonuses in each category (1st and 2nd place in each "good type"
get a bonus), announces the king and queen of each good type,
and then announces the winner. User can then look up individual player
scores and view score breakdown for that player."""



class PlayerScore(object):
    #object for each player's score. Maybe there's an easier way?
    def __init__(self, name):
        self.bread = 0 #initialize all the scores at zero, and the name as name
        self.cheese = 0
        self.chicken = 0
        self.apple = 0
        self.gold_coins = 0 #actual gold coin tokens
        self.final_score = 0
        self.contraband = 0
        self.name = name.upper()
        self.bonus = 0

    def total(self): #recalculate the total score, accounting for different gold value for each good type
        bread = self.bread * 3 #each of these calculates the gold value of the goods
        cheese = self.cheese * 3
        chicken = self.chicken * 4
        apple = self.apple * 2
        self.final_score = bread + self.bonus + cheese \
        				 + chicken + apple + self.contraband + self.gold_coins
        return self.final_score #make sure this function is not called more than once. Add a way to ensure this?

def reward(players, good):
    #give prizes for 1st and 2nd place for each good
    #todo: add actual values of prizes for 1st and 2nd place, they are not the same in the real game.
    prizes = {'chicken': (20, 10), 'apple': (10, 5), 'bread': (10, 5), 'cheese': (10, 5)} #dictionary stores value for each type
    king, queen = prizes[good]
    players = sorted(players, key = lambda x: getattr(x, good, 0))
    players[-1].bonus += king #top player is king, 2nd place is queen
    players[-2].bonus += queen
    print("{} is the king of {}, {} is the queen.".format(players[-1].name, good, players[-2].name))

players = [] # empty list of all player objects

while True: #this is kind of ugly?
    next_player = input("Next player name (or none to end): ")
    if next_player.lower() == "none":
        break #keep asking for player names until get "none"
    players.append(PlayerScore(next_player)) #add initialized score object to list of players, with next_player as player.name

for player in players: #get scores in each category for each player object
    player.apple = int(input('\n\nHow many apples did {} get? ' .format(player.name)))
    player.chicken = int(input('How many chickens did {} get? '.format(player.name)))
    player.cheese = int(input('How many cheese wheels did {} get? '.format(player.name)))
    if len(players) > 3: #bread is only included if there are more than 3 players
        player.bread = int(input('How many loaves of bread did {} get? '.format(player.name)))
    player.gold_coins = int(input('How many gold coins does {} have? '.format(player.name)))
    player.contraband = int(input('Shhh... what is {}\'s contraband score? '.format(player.name)))


print('\n\n')

for good in ['apple', 'chicken', 'cheese']:
    reward(players, good)

if len(players) > 3: #rather than these ifs all over for bread, just create a list that stores which goods are being used?
    reward(players, 'bread')
    
players.sort(key = lambda x: x.total()) #determine overall winner, simultaneously calling .total() on each
print('\n\n{} is the winner!'.format(players[-1].name))

while True: #allow lookup of player score breakdown
	lookup = input("\n\nPlayer whose score breakdown you wish to view: ").upper()
	if lookup not in [score.name for score in players]:
		print('Try again, that isn\'t a player.\n')
		continue #returns to beginning of while statement
	person = next(x for x in players if x.name == lookup) #I already forget what next() does? look into this.
	print('\nScore for {}.\nGold Pieces from: \n'.format(person.name))
	if len(players) > 3:
		print('BREAD: {}.\n'.format(person.bread))
	for good in ['chicken', 'apple', 'cheese', 'contraband', 'gold_coins', 'bonus']: #see, this is why a list of used goods would help
		print('{}s: {}.\n'.format(good.upper(), getattr(person, good)))
	
	

