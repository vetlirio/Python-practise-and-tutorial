# By changing the +/- on line five, sword either gain or loose health.
# Also by simply removing the f at the start of the parantases, it no longer prints the value of variable, but just the letters written, because its now just a string.

sword_damage = 10
start_health = 100
end_health = start_health - sword_damage
health_potion = 10
regained = start_health - sword_damage + health_potion
# Don't touch below this line
print(f"Sam's health is: {start_health}")
print(f"Sam takes {sword_damage} damage...")
print(f"Sam's health is: {end_health}")
print(f"Sam drinks health potion and gains: {health_potion} health points")
print(f"Sam's health is: {start_health}")
# could also use the variable "regained", instead of start_health
print(f"Sam has fully regained his health.... Sam's health back to {regained}")
print(regained)
