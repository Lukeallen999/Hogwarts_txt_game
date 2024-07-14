### Modules
import datetime
import random
import time
import functions.location_functions as loc
import functions.character_builder_functions as character
import functions.movement_functions as movement
import functions.map_functions as map

'-----------------------------------------------------------------'
### Variables
key = False
user_input = False
coords = [0,2]
#puppy_name = False
turn = 1
#from functions.location_functions import puppy_name
'''
character_name = input('Please enter your name: ')
character_gender = character.character_gender()
character_house = character.character_house()
'''

# Test to be deleted
character_name = 'Luke'
character_gender = 'Wizard'
character_house = 'Dragon'

class person:
    def __init__(self,name,profession,age,level) -> None:
        self.name = name
        self.profession = profession
        self.age = age
        self.level = level

# Characters
headmaster          = person(name = 'Professor Weasly',
                             profession = 'Headmaster',
                             age = 103,
                             level = 100)

defence_teacher     = person(name = 'Professor Longbottom',
                             profession = 'Defence teacher',
                             age = 35,
                             level = 20)

quidditch_teacher   = person(name = 'Professor Flume',
                             profession = 'Quidditch teacher',
                             age = 25,
                             level = 5)

potions_teacher     = person(name = 'Professor Walker',
                             profession = 'Potions teacher',
                             age = 88,
                             level = 61)

charms_teacher      = person(name = 'Professor Stone',
                             profession = 'Charms teacher',
                             age = 55,
                             level = 20)

brother             = person(name = 'Peter',
                             profession = 'Brother',
                             age = 18,
                             level = 1)

dad                 = person(name = 'Steven',
                             profession = 'Dad',
                             age = 63,
                             level = 1)

villain             = person(name = 'Casey Brown',
                             profession = 'Villain',
                             age = 19,
                             level = 7)

grounds_keeper      = person(name = 'Hagrid',
                             profession = 'Grounds keeper',
                             age = 154,
                             level = 3)




'-----------------------------------------------------------------'


### Main
# Intro
print(f'Hello {character_name}, {character_gender} of {character_house} house')



# Playing section
while user_input != 'EXIT':
    print(f'\n-------------- Turn: {turn} ----------------')
    turn +=1
    print(f'Coordinates: {coords}')	
    
    location = loc.location_dict[str(coords).replace(" ","")]
    print(f'You are in: {location}')
    next_turn = False
    map.update_map(coords,location)
    loc.run_location_function(coords)
    available_moves = movement.available_movement(coords)

    # This loop is used when the user teleports
    if loc.next_turn == True:
        loc.next_turn = False
        coords = loc.coords
        time.sleep(1)
        continue

    print('\nMove options:')
    for direction in available_moves:
        movement.move_options(direction)
    
    
    # Movement
    user_input = input('Move:').upper()
    coords = movement.movement(user_input,available_moves )
'-----------------------------------------------------------------'
