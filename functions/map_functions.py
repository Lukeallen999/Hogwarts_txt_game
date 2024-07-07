### Map Functions

blank_location_dict = {
'[0,4]':'Unknown','[1,4]':'Unknown','[2,4]':'Unknown','[3,4]':'Unknown','[4,4]':'Unknown',
'[0,3]':'Unknown','[1,3]':'Unknown','[2,3]':'Unknown','[3,3]':'Unknown','[4,3]':'Unknown',
'[0,2]':'Unknown','[1,2]':'Unknown','[2,2]':'Unknown','[3,2]':'Unknown','[4,2]':'Unknown',
'[0,1]':'Unknown','[1,1]':'Unknown','[2,1]':'Unknown','[3,1]':'Unknown','[4,1]':'Unknown',
'[0,0]':'Unknown','[1,0]':'Unknown','[2,0]':'Unknown','[3,0]':'Unknown','[4,0]':'Unknown'}

def map_table():
	print('|-------|-------|-------|-------|-------|')
	print('| [0,4] | [1,4] | [2,4] | [3,4] | [4,4] |')
	print('|--- ---|--- ---|--- ---|--- ---|--- ---|')
	print('| [0,3] | [1,3]   [2,3]   [3,3]   [4,3] |')
	print('|--- ---|-------|--- ---|--- ---|-------|')
	print('| [0,2]   [1,2]   [2,2]   [3,2]   [4,2] |')
	print('|-------|--- ---|--- ---|-------|--- ---|')
	print('| [0,1]   [1,1]   [2,1]   [3,1]   [4,1] |')
	print('|-------|-------|--- ---|-------|-------|')
	print('| [0,0]   [1,0]   [2,0]   [3,0]   [4,0] |')	
	print('|-------|-------|-------|-------|-------|')

def show_map():
	for coords, location in blank_location_dict.items():
		print(f'{coords}:{location}')
	print('')
	map_table()

def update_map(coords,location):
	coords = str(coords).replace(" ","")
	blank_location_dict.update({coords:location})
'-----------------------------------------------------------------'