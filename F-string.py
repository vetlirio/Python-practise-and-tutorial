# In Python we can create strings that contain dynamic values with the f-string syntax.

num_bananas = 10
f_string = f"You have {num_bananas} bananas"
print(f_string)
# You have 10 bananas
"""
    Opening quotes must be preceded by an f.
    Variables within curly brackets have their values "interpolated" (injected) into the string.
    It's just a string with a special syntax.
"""

# another example
name = "Yarl"
age = 37
race = "dwarf"

# Don't edit above this line

print(f"{name} is a {race} who is {age} years old.")

