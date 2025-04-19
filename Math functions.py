def HW():
    print("Hello, world!")
HW()



def greet(name):
    print("hello", name)
greet("Code-master!")



def greet(name):
    print("hello", name)
greet("Code-master!")


HW()
greet("Yah, boii!")


def space_line():
    print("   ")
space_line()



def cant_be(name):
    print("You cant be half-a-gangster,", name)
cant_be("Tony!")

space_line()

def mathing(functionspace):
    toes = 10
    addition = toes + functionspace
    return addition 

all_fingers = 10

total = mathing(all_fingers)

print(total)

space_line()
    
    
    
    
    
def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area


sword_length = 1.0
spear_length = 2.0

# don't touch above this line

sword_area = area_of_circle(sword_length)
spear_area = area_of_circle(spear_length)

# don't touch below this line

print("Sword length:", sword_length, "meters.")
print("Sword attack area:", sword_area, "square meters")

print("Spear length:", spear_length, "meters.")
print("Spear attack area:", spear_area, "square meters")
    
space_line()
space_line()

    
def area_of_circle(radius):
    pi = 3.14
    result = pi * radius * radius
    return result

radius = 5
meter = 10
ears = 2
area_radius = area_of_circle(radius)
area_meter = area_of_circle(meter)
area_ears = area_of_circle(ears)

print(area_radius)
print(area_meter)
print(area_ears)
space_line()
print(f"Here are all three in a row - radius, meter and ears: {area_radius}, {area_meter}, {area_ears}.")
