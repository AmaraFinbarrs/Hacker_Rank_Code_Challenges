"""
The whole point being that each player would like to make the height 1 of whatever tower it chooses,
because i evenly divide all other numbers. So the answer only depends on numbers of towers being odd or even,
except for the case when starting height of towers is 1, in that case player 1 always loses because it can't make any moves.
"""


def towerBreakers(n, m):
    # Write your code here
    
    number_tower, tower_length = n, m

    if tower_length == 1:
        return 2
    else :
        if number_tower % 2 == 0:
            return 2
        else:
            return 1