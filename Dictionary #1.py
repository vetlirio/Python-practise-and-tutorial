def get_character_record(name, server, level, rank):
    character = {"name": name, "server": server, "level": level, "rank": rank}
    return character

result = get_character_record("codemaster", 2, 20, 63)
print(result)



def get_character_record(name, server, level, rank):
    character = {"name": name, "server": server, "level": level, "rank": rank, "id": f"{name}#{server}"}
    return character

result = get_character_record("codemaster", "server1", 20, 63)

print(result)

