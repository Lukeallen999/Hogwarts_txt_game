import time
import textwrap

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

key = False
user_input = False
coords = [2,0]
puppy_name = False
turn = 1

### Location functions
location_dict = {
'[0,0]' : 'Hagrids hut',
'[0,1]' : 'Dorm',
'[0,2]' : 'The restricted section',
'[0,3]' : 'The Dungeons',
'[0,4]' : 'The room of requirements',
'[1,0]' : 'Womping Willow',
'[1,1]' : 'Common room',
'[1,2]' : 'Library',
'[1,3]' : 'Potions classroom',
'[1,4]' : 'Defence against the dark arts',
'[2,0]' : 'The Court yard',
'[2,1]' : 'Castle entrance',
'[2,2]' : 'The Great Hall',
'[2,3]' : 'Map Chamber',
'[2,4]' : 'Head Masters office',
'[3,0]' : 'The forbidden forrest',
'[3,1]' : 'Hospital wing',
'[3,2]' : 'Trophy room',
'[3,3]' : 'Astronomy Tower',
'[3,4]' : 'Charms classroom',
'[4,0]' : 'Deep in the forbidden forest',
'[4,1]' : 'Quidditch pitch',
'[4,2]' : "Moaning Myrtle's bathroom",
'[4,3]' : 'The stables',
'[4,4]' : 'The boat house'}
 

def run_location_function(coords):
    location_coords = str(coords).replace(" ","")
    location_coords = location_coords.replace("'","")
    location_coords = location_dict[location_coords].replace(" ","_") + '()'
    location_coords = location_coords.replace("'","")
    eval(location_coords)    

def print_clean_txt(txt: str) -> str:
    '''
    Helps increase readability of text in the terminal window 
    
    '''
    txt = txt.replace("  ","")
    txt = txt[1:]
    txt = textwrap.fill(txt, 100)

    print(txt)



def Hagrids_hut():
    global puppy_name     

    print_clean_txt('''
                    The pathway leading to Hagrid's hut was a journey in itself,
                    a testament to the half-giant's unique blend of practicality
                    and charm. It began with a winding, stony track that snaked
                    through the shadowed heart of the Hogwarts woodland, dappled
                    sunlight barely penetrating the thick canopy overhead. The
                    air hung heavy with the scent of damp earth and decaying
                    leaves, punctuated by the occasional pungent whiff of
                    something distinctly Hagrid-esque. Clumps of vibrant
                    mushrooms, their caps resembling tiny umbrellas, punctuated
                    the path, a touch of whimsical magic in the otherwise
                    austere setting. As the path deepened into the woods, the
                    air grew cooler, and the trees, gnarled and ancient, seemed
                    to press in closer, whispering secrets in the rustling
                    leaves. The gnarled roots of ancient oaks twisted across the
                    path, creating a natural obstacle course, forcing visitors
                    to clamber over them or carefully step around. Finally,
                    emerging from the dense undergrowth, the hut came into view,
                    a cozy, ramshackle abode built from rough-hewn logs and
                    topped with a thatched roof that seemed to sag under the
                    weight of years. A plume of smoke curled from the chimney,
                    promising warmth and hospitality within, welcoming any weary
                    traveller who dared to venture down the path.
                    ''')
    print('')
    print_clean_txt('''
                    The door creaked open, revealing a scene of utter chaos. The
                    lingering scent of something dark and sinister. You
                    frantically search the room, your hands trembling, a knot of
                    fear twisting in your gut. Where were his creatures? The
                    giant spider, Aragog, had vanished from his terrarium,
                    leaving behind only a single, silken thread,
                    stretching towards the dark woods beyond. His beloved
                    Blast-Ended Skrewt, usually kept in a secure cage, had left
                    a trail of destruction in its wake, its sharp claws tearing
                    at the wood of the floorboards. A sense of dread washes over
                    you, a gnawing fear that something terrible had happened,
                    something that threatened not only Hagrid's home, but the
                    very safety of Hogwarts. You know, with a certainty that
                    chills you to the bone, that this wasn't just a simple
                    break-in, this was something far darker, a deliberate act of
                    sabotage, aimed at Hagrid and the creatures he cared for.
                    ''')
    print('')
    if puppy_name == False:
        print_clean_txt('''
                        A whimper, soft and pathetic, coming from the wreckage
                        of Hagrid's once-cozy home. The place was in chaos -
                        furniture overturned, shelves emptied, everything coated
                        in a layer of dust and broken glass. The scent of burnt
                        wood lingered, a bitter reminder of the fire that had
                        ravaged the place. You cautiously step over a broken
                        table, your heart pounding in my chest. The whimper came
                        again, closer this time, and you freeze. It was from the
                        rubble of the fireplace, where a pile of charred logs
                        lay smouldering.
                        ''')
        print('')
        choice_input = input('Do you investigate? (Y/N):').upper()
        if choice_input == 'Y':
            print_clean_txt('''
                            As you move closer, you see a small, furry creature
                            huddled beneath the debris, its whimpers growing
                            louder, punctuated by panicked gasps. It was a
                            small, brown dog, its fur matted and its eyes wide
                            with fear. It had clearly been injured, a cut on its
                            leg oozing blood. I knelt down, gently coaxing it
                            out from under the logs, and as I cradled it in my
                            arms, I realized this little creature was the sole
                            survivor of this attack, the only one who could tell
                            the story of what had happened here. A story that, I
                            knew, would be filled with fear, danger, and
                            perhaps, the terrible truth about the attack on
                            Hagrid's hut.
                            ''')
            puppy_name = input('You decide to call the puppy:' )
            print(f'Good {puppy_name} you say as you pet you new found friend')



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
        if puppy_name != False:
               print(f'You have a puppy called {puppy_name}')
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