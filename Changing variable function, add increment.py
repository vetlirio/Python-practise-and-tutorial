# updating variable with a function, adding increment to current score.

def update_player_score(current_score, increment):
    current_score = current_score + increment
    return current_score

print(update_player_score(5, - 2))
    
    
star_rating = 4
star_rating -= 1
# star_rating is now 3

star_rating = 4
star_rating *= 2
# star_rating is now 8

star_rating = 4
star_rating /= 2
# star_rating is now 2.0