def check_high_score(player_name, high_scoring_player_name, low_scoring_player_name):
    if player_name == high_scoring_player_name:
       return "high"
    elif low_scoring_player_name == player_name:
        return "low" 
    else:
         return "neither"



def player_status(health):
    if health <= 0:
       return "dead"
    elif health <= 5:
        return "injured"
    else: 
        return "healthy"