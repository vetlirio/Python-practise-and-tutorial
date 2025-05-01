# list, dictionary and set

🔹 List  → [ item1, item2, item3 ]
- Ordered
- Can change
- Allows duplicates

🔸 Dictionary  → { key1: value1, key2: value2 }
- Key-value pairs
- No duplicate keys

🔺 Set  → { item1, item2, item3 }
- Unordered
- No duplicates
- No index access

⚠️ {} = empty dictionary
⚠️ Use set() for an empty set



check type:
    fruits = {"apple", "banana", "grape"}
print(type(fruits))


Because the empty bracket {} syntax creates an empty dictionary, to create an empty set, you need to use the set() function.
fruits = set()
fruits.add("pear")
print(fruits)
# Prints: {'pear'}

# for sets iteration
fruits = {"apple", "banana", "grape"}
for fruit in fruits:
    print(fruit)
    # Prints:
    # banana
    # grape
    # apple
    
    
    # example of getting two list with some of the same names on them. By putting both list in a set, the duplicates go away,
    # then by converting it to a list again, its now a list with no duplicates.
    def remove_duplicates(spells):
    new_set = set()
    new_list = []
    for spell in spells:
        new_set.add(spell)
        new_list = list(new_set)
    return new_list
        
    .add() ## in order to add to sett 