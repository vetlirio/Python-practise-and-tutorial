def process_player_record(player_id):
    try: 
        return get_player_record(player_id)
    except IndexError:
        return "index is too high"
    except Exception as e:
        return e
        
try:
    raise Exception("zero division")
except ZeroDivisionError as e:
    print("zero")
except Exception as e:
    print("other")



## actuall example of raising exeption: In the game the player can buy things even when there issent enough gold.
    
    def purchase_item(price, gold_available):
    if gold_available >= price:
        return gold_available - price
    else:
        raise Exception("not enough gold")
            
  