def main():
    try:    
        print(get_player_record(1))
        print(get_player_record(2))
        print(get_player_record(3))
        print(get_player_record(4))
    except Exception as e:
        print(e)


# try (try-blokk) is for handling expetions.
# instead of printing ERROR, its just prints "player id not found"
# the code can run smoothly without ERROR in it, because exceptions are handled thru try.

# e is the variable for Exceptions.
  ##  except Exception as e:
  ##  if you dont have except, python woundt know its an expetion (compared to a normal variable)



## raising exceptions

def get_player_record(player_id):
    if player_id == 1:
        return {"name": "Slayer", "level": 128}
    if player_id == 2:
        return {"name": "Dorgoth", "level": 300}
    if player_id == 3:
        return {"name": "Saruman", "level": 4000}
    raise Exception("player id not found")

