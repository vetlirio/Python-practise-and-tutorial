
def cast_iceblast(dmg, mana):
    total = mana - dmg
    return dmg, total 

#1
dmg, mana = cast_iceblast(5, 100)
print(f"Damage: {dmg}, Remaining Mana: {mana}")
# Damage: 5, Remaining Mana: 95

#2
firebreath, life_i_got_left = cast_iceblast(50, 250)
print(F"firebreath took {firebreath} damage, and now I got {life_i_got_left} mana left")

# Why issent second one returning 200 from mana?