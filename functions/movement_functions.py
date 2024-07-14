  ### Movement
### Functions
import functions.location_functions as loc
## Movement 
coords = [2,0]
move_dict = {
'N':1,
'S':-1,
'E':1,
'W':-1}

def movement(direction,available_moves):
	if direction in available_moves: 
		if direction in ['N','S']:
			coords[1] += move_dict[direction]
		if direction in ['E','W']:
			coords[0] += move_dict[direction]
	else:
			print("You can't go that way")
	
	return coords

def move_options(direction):
	if direction in ['N','S']:
		location = [coords[0],coords[1] + move_dict[direction]]
	if direction in ['E','W']:
		location = [coords[0] + move_dict[direction],coords[1]]
	
	location = str(location).replace(" ","")
	
	if location in loc.location_dict.keys():		
		location = loc.location_dict[location]
		print(f'{direction}: {location}')	

# Teleport
def teleport(x_coord, y_coord):
	global coords
	coords = [x_coord,y_coord]
	return coords		
'-----------------------------------------------------------------'

## Available movement
available_movement_dict = {
'[0,0]':'E',
'[0,1]':'E',
'[0,2]':'N,E',
'[0,3]':'N,S',
'[0,4]':'S',
'[1,0]':'E,W',
'[1,1]':'N,E,W',
'[1,2]':'E,S,W',
'[1,3]':'E',
'[1,4]':'S',
'[2,0]':'N,E,W',
'[2,1]':'N,E,S,W',
'[2,2]':'N,E,S,W',
'[2,3]':'N,E,S,W',
'[2,4]':'S',
'[3,0]':'E,W',
'[3,1]':'E,W',
'[3,2]':'N,E,W',
'[3,3]':'N,E,S,W',
'[3,4]':'S',
'[4,0]':'N,W',
'[4,1]':'N,W',
'[4,2]':'S,W',
'[4,3]':'N,W',
'[4,4]':'S',

}

def available_movement(coords):
		available_coords = str(coords).replace(" ","")
		available_movement = available_movement_dict[available_coords]
		available_movement = available_movement.split(',')
		return available_movement
'-----------------------------------------------------------------'