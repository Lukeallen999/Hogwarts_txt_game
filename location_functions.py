### Location functions
location_dict = {
'[0,0]': 'Hagrids hut',
'[0,1]': 'Dorm',
'[0,2]':'The restricted section',
'[0,3]':'The Dungeons',
'[0,4]':'The room of requirements',
'[1,0]':'Womping Willow',
'[1,1]':'Common room',
'[1,2]':'Library',
'[1,3]':'Potions classroom',
'[1,4]':'Defence against the dark arts',
'[2,0]':'The Court yard',
'[2,1]':'Castle entrance',
'[2,2]':'The Great Hall',
'[2,3]':'Map Chamber',
'[2,4]':'Head Masters office',
'[3,0]':'The forbidden forrest',
'[3,1]':'Hospital wing',
'[3,2]':'Trophy room',
'[3,3]':'Astronomy Tower',
'[3,4]':'Charms classroom',
'[4,0]':'Deep in the forbidden forest',
'[4,1]':'Quidditch pitch',
'[4,2]':"Moaning Myrtle's bathroom",
'[4,3]':'The stables',
'[4,4]':'The boat house'}


def run_location_function(coords):
    location_coords = str(coords).replace(" ","")
    location_coords = location_coords.replace("'","")
    location_coords = location_dict[location_coords].replace(" ","_") + '()'
    location_coords = location_coords.replace("'","")
    eval(location_coords)    


def Hagrids_hut():
        print("You are in: Hagrids hut")
def Dorm():
        print("You are in: Dorm")
def The_restricted_section():
        print("You are in: The restricted section")
def The_Dungeons():
        print("You are in: The Dungeons")
def The_room_of_requirements():
        print("You are in: The room of requirements")
def Womping_Willow():
        print("You are in: Womping Willow")
def Common_room():
        print("You are in: Common room")
def Library():
        print("You are in: Library")
def Potions_classroom():
        print("You are in: Potions classroom")
def Defence_against_the_dark_arts():
        print("You are in: Defence against the dark arts")
def The_Court_yard():
        print("You are in: The Court yard")
def Castle_entrance():
        print("You are in: Castle entrance")
def The_Great_Hall():
        print("You are in: The Great Hall")
def Map_Chamber():
        print("You are in: Map Chamber")
        print('Up on the wall you see a giant map of Hogwarts')
        user_input = input('Do you look at the map?\n(Y/N):').upper()		
        if user_input == 'Y':
                print('y')
        	#show_map()
def Head_Masters_office():
        print("You are in: Head Masters office")
def The_forbidden_forrest():
        print("You are in: The forbidden forrest")
def Hospital_wing():
        print("You are in: Hospital wing")
def Trophy_room():
        print("You are in: Trophy room")
def Astronomy_Tower():
        print("You are in: Astronomy Tower")
def Charms_classroom():
        print("You are in: Charms classroom")
def Deep_in_the_forbidden_forest():
        print("You are in: Deep in the forbidden forest")
def Quidditch_pitch():
        print("You are in: Quidditch pitch")
def Moaning_Myrtles_bathroom():
        print("You are in: Moaning Myrtle's bathroom")
def The_stables():
        print("You are in: The stables")
def The_boat_house():
        print("You are in: The boat house")