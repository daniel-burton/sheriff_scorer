class PlayerScore(object):
    #object for each player's score
    def __init__(self, name):
        self.bread = 0 #initialize all the scores at zero, and the name as name
        self.cheese = 0
        self.chicken = 0
        self.apple = 0
        self.final_score = 0
        self.contraband = 0
        self.name = name.upper()
        self.bonus = 0 #this is ugly, should be included with category score.

    def total(self): #recalculate the total score
        self.bread = self.bread * 3 #each of these calculates the gold value of the goods
        self.cheese = self.cheese * 3
        self.chicken = self.chicken * 4
        self.apple = self.apple * 2
        self.final_score = self.bread + self.bonus +  self.cheese \
        				 + self.chicken + self.apple + self.contraband
        return self.final_score

def reward(players, good):
    #give prizes for 1st and 2nd place for each good
    prizes = {'chicken': (10, 5), 'apple': (10, 5), 'bread': (10, 5), 'cheese': (10, 5)}
    king, queen = prizes[good]
    players.sort(key = lambda x: getattr(x, good, 0))
    players[-1].bonus += king
    players[-2].bonus += queen
    print("{} is the king of {}, {} is the queen.".format(players[-1].name, good, players[-2].name))

players = [] #list of all player names

while True:
    next_player = input("Next player name (or none to end): ")
    if next_player.lower() == "none":
        break #keep asking for player names until get "none"
    players.append(PlayerScore(next_player)) #add empty score object to list of players

for player in players: #get scores in each category for each player object
    player.apple = int(input('\n\nHow many apples did {} get? ' .format(player.name)))
    player.chicken = int(input('How many chickens did {} get? '.format(player.name)))
    player.cheese = int(input('How many cheeses did {} get? '.format(player.name)))
    if len(players) > 3:
        player.bread = int(input('How many loaves of bread did {} get? '.format(player.name)))
    player.contraband = int(input('Shhh... what is {}\'s contraband score? '.format(player.name)))


print('\n\n')

for good in ['apple', 'chicken', 'cheese']:
    reward(players, good)

if len(players) > 3:
    reward(players, 'bread')
    
players.sort(key = lambda x: x.total())
print('\n\n{} is the winner!'.format(players[-1].name))

while True:
	lookup = input("\n\nPlayer whose score breakdown you wish to view: ").upper()
	if lookup not in [score.name for score in players]:
		print('Try again, that isn\'t a player.\n')
		continue
	person = next(x for x in players if x.name == lookup)
	print('\nScore for {}.\n Gold Pieces from: \n'.format(person.name))
	if len(players) > 3:
		print('BREAD: {}.\n'.format(person.bread))
	for good in ['chicken', 'apple', 'cheese', 'contraband', 'bonus']:
		print('{}s: {}.\n'.format(good.upper(), getattr(person, good)))
	
	

