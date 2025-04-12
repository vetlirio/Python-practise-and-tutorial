"""
    The max players on a "small" server: 1,024,000,000,000,000,000 (1.024e18)
    The max players on a "medium" server: 10,240,000,000,000,000,000
    The max players on a "large" server: 102,400,000,000,000,000,000

    Count the number after the first number. its not how many zero's, but how many times to the power of ten.
    
    Medium is 1 times larger then small, and large is 100 times larger then small.
"""




def max_players_on_server():
    small = 1.024e18
    medium = 1.024e19
    large = 1.024e20
    return small, medium, large 

print(max_players_on_server())
    