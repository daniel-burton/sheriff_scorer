"""this program creates a "player score" object for each
player (from an interactive text prompt) and then gets the
scores in each category for each player. It then calculates the
bonuses in each category (1st and 2nd place in each "good type"
get a bonus), announces the king and queen of each good type,
and then announces the winner. User can then look up individual player
scores and view score breakdown for that player."""

class PlayerScore(object):
    def __init__(self, name):
        # initialize all the scores at zero, name as name
        self.bread = 0
        self.cheese = 0
        self.chicken = 0
        self.apple = 0
        self.gold_coin = 0  # actual gold coin tokens
        self.final_score = 0
        self.contraband = 0
        self.name = name.upper()  # uppercase is more fun
        self.bonus = 0

    def total(self):
        """recalculate the total score, accounting for different gold value
        for each good type"""
        # each of these calculates gold value of the good
        self.bread = self.bread * gold_values['bread']
        self.cheese = self.cheese * gold_values['cheese']
        self.chicken = self.chicken * gold_values['chicken']
        self.apple = self.apple * gold_values['apple']
        self.final_score = (self.bread + self.bonus + self.cheese
                            + self.chicken + self.apple + self.contraband
                            + self.gold_coin)
        return self.final_score

def reward(players, good):
    # give prizes for 1st and 2nd place for each good
    prizes = {'chicken': (20, 10), 'apple': (10, 5),
              'bread': (10, 5), 'cheese': (10, 5),
              'contraband': (0, 0), 'gold': (0, 0)}
    king, queen = prizes[good]
    players = sorted(players, key=lambda x: getattr(x, good, 0))
    players[-1].bonus += king  # top player is king, 2nd place is queen
    players[-2].bonus += queen
    print("{} is the {} king, {} is the queen.".format(players[-1].name,
                                                       good,
                                                       players[-2].name))

def ask_score(player, good):
    """create the string to ask the score for each good to eliminate
    duplicate code"""
    ask = {"apple": "many apples", "bread": "many loaves of bread",
           "cheese": "many wheels of cheese", "chicken": "many chickens",
           "contraband": "much contraband", "gold": "many gold coins"}
    score = int(input("How {} did {} get? ".format(ask[good], player.name)))
    return score

players = []  # empty list of all player objects

gold_values = {'apple': 2, 'bread': 3, 'cheese': 3, 'chicken': 4,
               'contraband': 1, 'bonus': 1, 'gold_coin': 1}

if __name__ == "__main__":
    while True:
        next_player = input("Next player name (or none to end): ")
        if next_player.lower() == "none" or next_player.lower() == "":
            break  # keep asking for player names until get "none"
        players.append(PlayerScore(next_player))
        # add initialized score object to list of players

    goods = ['apple', 'cheese', 'chicken', 'contraband', 'gold']
    if len(players) > 3:
        goods.append('bread')

    for player in players:  # get score in each category for each player object
        for item in goods:
            player.item = ask_score(player, item)

    print('\n\n')

    for item in goods:
        reward(players, item)

    players.sort(key=lambda x: x.total(), reverse=True)
    # determine overall winner, simultaneously calling .total() on each
    print('\n\n{} is the winner!'.format(players[0].name))

    while True:  # allow lookup of player score breakdown
        lookup = input(("\n\nPlayer whose score breakdown you wish to view"
                        " (or hit enter to end program): """)).upper()
        if lookup == "":
            print("Thanks for playing!\n")
            break
        if lookup not in [score.name for score in players]:
            print("Try again, that isn't a player.\n")
            continue  # returns to beginning of while statement
        person = next(x for x in players if x.name == lookup)
        print('\nScore for {}.\nGold Pieces from: \n'.format(person.name))
        if len(players) > 3:
            print('BREAD: {}.\n'.format(person.bread * gold_values['bread']))
        for item in ['chicken', 'apple', 'cheese', 'contraband', 'gold_coin',
                     'bonus']:
            print('{}: {}.\n'.format(item.upper(),
                                     getattr(person, item)))
