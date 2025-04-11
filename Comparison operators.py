# When coding it's necessary to be able to compare two values. Boolean logic is the name for these kinds of comparison operations that always result in True or False.

# The operators:
"""
    < "less than"
    > "greater than"
    <= "less than or equal to"
    >= "greater than or equal to"
    == "equal to"
    != "not equal to"
"""
"""For example:

5 < 6 # evaluates to True
5 > 6 # evaluates to False
5 >= 6 # evaluates to False
5 <= 6 # evaluates to True
5 == 6 # evaluates to False
5 != 6 # evaluates to True
"""

def player_1_wins(player_1_score, player_2_score):
    Has_higher_score = player_1_score > player_2_score
    return Has_higher_score

print(player_1_wins(4134, 2341))



def player_status(health):
    if health <= 0:
       return "dead"
    elif health <= 5:
        return "injured"
    else: 
        return "healthy"
    
    
    some rules
   # You can't have an elif or an else without an if
   # You can have an else without an elif
