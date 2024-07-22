import random

class enemey:
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
          

def fight(character_name,enemy_name):
    character_name = eval('character_name')
    enemy_name = eval('enemy_name')

    if character_name == user_character:
        attack_choice = int(input('Please choose an attack from 1-3: '))
        attack_type, attack_name, attack_damage, attack_chance = character_name.attack[attack_choice]

    else:     
        attack_type, attack_name, attack_damage, attack_chance = character_name.attack[random.choice(list(user_character.attack.keys()))]
    
    print(f'{character_name.name} uses: {attack_name} ({attack_type}) ')
    if random.randint(1,10) <= (attack_chance * 10):
        print(f'{character_name.name}: Hit for {attack_damage} damage')
        enemy_name.health -= attack_damage
    else:
        print(f'{character_name.name}: Miss') 


fight_round = 0
print(f'Moves:')
for attack in user_character.attack.keys():
    attack_type, attack_name, attack_damage, attack_chance = user_character.attack[attack]
    print(f'Option: {attack}')
    print(f'Attack Type: {attack_type}')
    print(f'Attack: {attack_name}')
    print(f'Damage: {attack_damage}')
    print(f'Chance: {attack_chance*100}%\n')

while troll.health > 0 and user_character.health > 0:
    print(f'-------------------- Round:{fight_round} --------------------')
    fight(user_character,troll)
    fight(troll,user_character)

    print('')
    print(f'User Health: {user_character.health}')
    print(f'troll Health: {troll.health}')
    
    print('')
    print('')
    fight_round += 1
print('Please pick an attack using numbers 1,2,3')




