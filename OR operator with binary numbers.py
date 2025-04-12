# OR operator with binary numbers, combinging all players permission into one,
# due to being on same team


def calculate_guild_perms(glorfindel, galadriel, elendil, elrond):
    Combined_permission = glorfindel | galadriel | elendil | elrond
    return Combined_permission

print(calculate_guild_perms(0b1000, 0b0100, 0b0010, 0b0001))