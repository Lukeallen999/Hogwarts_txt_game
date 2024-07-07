### Character Builder
gender_dict = {
	1: 'Wizard',
	2: 'Witch' }

def character_gender(gender_checker = False	):
    while gender_checker == False:
        print('Gender options: ')
        for num,name in gender_dict.items():
            print(f'{num}:{name}')
        
        gender = int(input('Please enter the number for either Wizard or Witch: '))
        
        gender_checker = gender in gender_dict.keys()
        
        if gender_checker == True:
            gender = gender_dict[gender]
            gender_checker = input(f'You have selected to be a {gender} \nis this correct? (Y/N): ')
            if gender_checker != 'Y':
                gender_checker = False
        else:
            print('Stop fucking about')
    return(gender)
'-----------------------------------------------------------------'

# House 
house_dict = {
	1: 'Gryffindor',
	2: 'Slytherin',
	3: 'Ravenclaw',
	4: 'Hufflepuff' }

def character_house(house_checker = False):
    while house_checker == False:
        print('House options:')
        for num,name in house_dict.items():
            print(f'{num}:{name}')
        
        house = int(input('Please enter the number of the house you would like: '))
        house_checker = house in house_dict.keys()
        
        if house_checker == True:
            house = house_dict[house]
            house_checker = input(f'You have selected {house} house \nis this correct? (Y/N): ')
            if house_checker != 'Y':
                house_checker = False
        else:
            print('Stop fucking about')
    print(f'House is {house}')
    return house
'-----------------------------------------------------------------'
