# Multi-Variable Declaration

# We can save space when creating many new variables by declaring them on the same line:

sword_name, sword_damage, sword_length = "Excalibur", 10, 200

# Which is the same as:

sword_name = "Excalibur"
sword_damage = 10
sword_length = 200

# Any number of variables can be declared on the same line,
# and variables declared on the same line should be related to one another in some way so that the code remains easy to understand.

# We call code that's easy to understand "clean code".

print(f"All the values in the line above is in this line {sword_name}, {sword_damage}, {sword_length}")

filler_line = "   "

quest_start = "You there! Adventurer!"
quest_middle = "The local mine has been taken over by orcs!"
quest_end = "We need your help taking it back."
quest_objective = "Bring back 8 of their axes as proof of your hard work."
space = " "

# don't touch above this line
print(filler_line)
print(quest_start)
print(quest_middle)
print(quest_end + space + quest_objective)