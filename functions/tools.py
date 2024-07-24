# Modules
import random
import time
import characters_class as character

'''class enemey:
    def __init__(self, name, health, attack) -> None:
        self.name = name
        self.health = health
        self.attack = attack
   
class main_character:
    def __init__(self, name, health, attack) -> None:
        self.name = name
        self.health = health
        self.attack = attack
        
user_character = main_character(name = 'User',
                                health = 50,
                                attack = {
                                1 : ['Light attack','Punch', 5, 0.8],
                                2 : ['Medium attack','Kick', 10, 0.5],
                                3 : ['Heavy attack','Spell', 20, 0.2]
                                } 
                                )    

   
troll = enemey(name = 'troll',
               health = 50,
               attack = {
               1 : ['Light attack','Club Swipe', 5, 0.8],
               2 : ['Medium attack','Roar', 10, 0.5],
               3 : ['Heavy attack','Club Smash', 20, 0.2]
               } 
               )
          '''



def attack_options() -> None:
    '''
    Prints a list of possible moves for the user
    '''
    
    print(f'Moves:')
    for attack in character.user_character.attack.keys():
        attack_type, attack_name, attack_damage, attack_chance = character.user_character.attack[attack]
        print(f'Option: {attack}')
        print(f'Attack Type: {attack_type}')
        print(f'Attack: {attack_name}')
        print(f'Damage: {attack_damage}')
        print(f'Chance: {attack_chance*100}%\n')

def attack_action(attacker: str, target: str) -> None:
    '''
    Uses Classes to get the values and then prints an attack against a target
    '''

    # Uses Eval to get the class needed
    attacker = eval('attacker')
    target = eval('target')

    # Alows the user to choose what attack they want and to see attack options
    if attacker == character.user_character:       
        if input('Do you want to see move options?(Y/N): ').upper() == 'Y':
            attack_options()
        attack_choice = int(input('Please choose an attack from 1-3: '))
        attack_type, attack_name, attack_damage, attack_chance = attacker.attack[attack_choice]
    else:     
        attack_type, attack_name, attack_damage, attack_chance = attacker.attack[random.choice(list(character.user_character.attack.keys()))]
    
    print(f"\n---- {attacker.name}'s turn ----")
    print(f'{attacker.name} uses: {attack_name} ({attack_type}) ')

    # Determins if attack hits and then deals damage
    if random.randint(1,10) <= (attack_chance * 10):
        print(f'{attacker.name}: Hit for {attack_damage} damage')
        target.health -= attack_damage
    else:
        print(f'{attacker.name}: Miss') 

def battle(character_name,enemy_name):

    '''
    Prints an interative battle between two characters
    '''

    fight_round = 1
    
    while character_name.health > 0 and enemy_name.health > 0:
        print(f'-------------------- Round:{fight_round} --------------------')
        
        attack_action(attacker = character_name, target = enemy_name)
        print('')
        time.sleep(1)

        attack_action(attacker = enemy_name,target = character_name)
        print('')

        print(f'User Health: {character.user_character.health}')
        print(f'troll Health: {character.troll.health}')
        
        print('')
        fight_round += 1

        if character_name.health <= 0:
            print('YOU LOSE')
            exit()
        
        if enemy_name.health <= 0:
            print('You Win')
        
        
        input('PRESS ENTER')
        print('')
        

battle(character.user_character,character.troll)