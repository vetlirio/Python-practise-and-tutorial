# iterating over a dictionary
fruit_sizes = {
    "apple": "small",
    "banana": "large",
    "grape": "tiny"
}

for name in fruit_sizes:
    size = fruit_sizes[name]
    print(f"name: {name}, size: {size}")
    
    
print(fruit_sizes)


for name in fruit_sizes:
    size = fruit_sizes[name]
    print(name, size)
    
    
def get_most_common_enemy(enemies_dict):
    max_so_far = float("-inf")
    most_common = None
    for enemy_name in enemies_dict:
        count = enemies_dict[enemy_name]
        if count > max_so_far:
            max_so_far = count
            most_common = enemy_name
    return most_common
            
