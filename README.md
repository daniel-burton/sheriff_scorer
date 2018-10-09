# sheriff_scorer
Calculates final scores for the game Sheriff of Nottingham. Practice for object-oriented programming concepts.

In this game, players attempt to sneak goods and contraband past the "sheriff." The player with the most
gold at the end of the game wins. Each product is worth a different amount of gold, and there are also bonuses given to the top two players for each product (top apple merchant, top wheat merchant, etc).

This program creates score objects for each player, and then accepts scores for each category. It then calculates and allocates the bonuses and total scores and declares the winner.

The user can request a score breakdown for each player and view that player's score.

To do: 
* should the trade goods have a class, or just be dictionaries?
* the player_score objects are stored in a list with no names. Would giving them names make the program clearer?
* Just realized there's no need for the total() function, why not just multiply each type of good by the gold amount as they are collected.
