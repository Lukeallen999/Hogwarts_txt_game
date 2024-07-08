### Modules
import datetime
import random
import functions.location_functions as loc
import functions.character_builder_functions as character
import functions.movement_functions as movement
import functions.map_functions as map
'-----------------------------------------------------------------'
### Variables
key = False
user_input = False
coords = [2,0]
puppy_name = False
turn = 1
'''
character_name = input('Please enter your name: ')
character_gender = character.character_gender()
character_house = character.character_house()
'''

# Test to be deleted
character_name = 'Luke'
character_gender = 'Wizard'
character_house = 'Dragon'


# Characters
head_master = 'Professor Weasly'
defence_teacher = 'Professor Longbottom'
quidditch_teacher = 'Professor Flume'
potions_teacher = 'Professor Walker'
charms_teacher = 'Professor Stone'
brother = 'Peter'
dad = 'Steven'
villain = 'Casey Brown'
grounds_keeper = 'Hagrid'
'-----------------------------------------------------------------'


### Main
# Intro
print(f'Hello {character_name}, {character_gender} of {character_house} house')



# Playing section
while user_input != 'EXIT':
    print(f'\n-------------- Turn: {turn} ----------------')
    print(f'Coordinates: {coords}')	


    location = loc.location_dict[str(coords).replace(" ","")]
    print(f'You are in: {location}')
    map.update_map(coords,location)
    loc.run_location_function(coords)
    available_moves = movement.available_movement(coords)

    print('\nMove options:')
    for direction in available_moves:
        movement.move_options(direction)
    

    # Movement
    user_input = input('Move:').upper()
    coords = movement.movement(user_input,available_moves )
    turn +=1
'-----------------------------------------------------------------'
