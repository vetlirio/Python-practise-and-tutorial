kokiri_sword = 1
master_sword = 2
biggoron_sword = 4


def fight_bongo(sword, hits):
    damage = sword * hits 
    new_health = 32 - damage
    return new_health

kokiri = 1 
biggoron = 4
light_arrow = 8
print(f"After Bongobongo was hit 7 times with the kokiri sword his health (hp) went from 32 to {fight_bongo(kokiri, 7)}")

print("but....another player went to into the boss fight with a different sword that was much more effective and....")
print(f"after Bongobongo was hit 6 times with the Biggoron sword his hp went from 32 to {fight_bongo(biggoron, 4)}.....")
print("Sure enough, that was very impressive, but then one day a a warrior went to the shadow temple...")
print(f"the warrior fired 4 light-arrows straight into Bongobongo before he even knew what was happening and his hp went from 32 to {fight_bongo(light_arrow, 4)}")
print("Bongobongo was defeated in under 5 seconds....")

