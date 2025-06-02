list_of_numbers = [5, 2, 16, 23, 56, 67]
sorted_list = sorted(list_of_numbers)
print(sorted_list)

#sorting in place
list_of_numbers.sort()
print(list_of_numbers)

#passing functions into sorted 
list_of_orders = ["apple", "banana", "cherry"]
print("Basic Sorting", sorted(list_of_orders))

sorted_by_length = sorted(list_of_orders, key=len)
print("Sorted by length", sorted_by_length)

def orders_sorting(string):
    return int(string[1:])

sorted_by_size = sorted(list_of_orders, key=orders_sorting)
print("Sorted by size", sorted_by_size)

#Working with Pokedex

list_of_pokemon = {
    1: {"name": "Bulbasaur", "type": "Grass/Poison", "hp": 45},
    4: {"name": "Charmander", "type": "Fire", "hp": 39},
    7: {"name": "Squirtle", "type": "Water", "hp": 44},
    25: {"name": "Pikachu", "type": "Electric", "hp": 35},
    39: {"name": "Jigglypuff", "type": "Normal/Fairy", "hp": 115},
    94: {"name": "Gengar", "type": "Ghost/Poiso n", "hp": 60},
    143: {"name": "Snorlax", "type": "Normal", "hp": 160},
}

def sorted_by_pokedex(pokemon):
    return pokemon['pokedex']

sorted(list_of_pokemon, key=sorted_by_pokedex, reverse=True)

#Map Function
list_of_nums =[1,2,3,4 ,5]

def square(num):
    return num **2 
print(list(map(square, list_of_numbers)))

#Lamda functions 
print(list(map(lamda num: num ** 2, list_of_numbers)))
print(new_list)

greetings = ["hello", "hi", "hey"]
#length of strings in a list witgh for loops 
length_of_greetings = []
for greeting in greetings:
    length_of_greetings.apend(len(greetings))
print(length_of_greetings)


length_of_greetings = list(map(lamda x: len(x), greetings))
print(length_of_greetings)

first_names  =   [" John ","Jane", "Timothy"]
last_names  =   ["Mike","Jerry", "Kim"]

full_names = list(map(lamda x,y, : x + "" + y, first_names, last_names))
print(full_names)

#Using Filter functions
list_of_nums =[1,2,3,4 ,5]
odds = []

#With for loop
for num in list_of_nums:
    if num % 2 == 1:
        odds.append(num)
print(odds)

odds = list(filter(lamda num: num % 2 == 1, list_of_nums))
print(odds)


greetings = ["hello", "hi", "hey"]
short_greetings =list( filter(lamda x: len(x) < 5, greetings))