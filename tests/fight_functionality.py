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
                                'Light_attack' : ['Light attack', 5, 0.8],
                                'Medium_attack' : ['Medium attack', 10, 0.5],
                                'Heavy_attack' : ['Heavy attack', 20, 0.2]
                                } 
                                )    

   
troll = enemey(name = 'troll',
               health = 50,
               attack = {
               'Light_attack' : ['Light attack', 5, 0.8],
               'Medium_attack' : ['Medium attack', 10, 0.5],
               'Heavy_attack' : ['Heavy attack', 20, 0.2]
               } 
               )

               



'''health = troll.health
print(health)
health -= 1
print(health)'''





for i in range(0,10):
    attack_name, attack_damage, attack_chance = random.choice(list(troll.attack.items()))
    print(f' Attack = {attack_name} damage = {attack_damage} chance = {attack_chance}')
    print('')


fight_round = 0
while troll.health > 0 or user_character.health > 0:
    print(f'-------------------- Round:{fight_round} --------------------')
    print(f'Moves:')
    print(f'{user_character.attack[0]}')

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
                                'Light_attack' : ['Light attack', 5, 0.8],
                                'Medium_attack' : ['Medium attack', 10, 0.5],
                                'Heavy_attack' : ['Heavy attack', 20, 0.2]
                                } 
                                )    

   
troll = enemey(name = 'troll',
               health = 50,
               attack = {
               'Light_attack' : ['Light attack', 5, 0.8],
               'Medium_attack' : ['Medium attack', 10, 0.5],
               'Heavy_attack' : ['Heavy attack', 20, 0.2]
               } 
               )

               



'''health = troll.health
print(health)
health -= 1
print(health)'''




'''
print('')
for i in range(0,10):
    choice = random.choice(troll.attack)
    print(choice)
    print(f' Attack = {choice[0]} damage = {choice[1]}')
    print('')
'''

print('')
for i in range(0,10):
    attack_name, attack_damage, attack_chance = random.choice(list(troll.attack.items()))
    print(choice)
    print(f' Attack = {attack_name} damage = {attack_damage} chance = {attack_chance}')
    print('')


fight_round = 0
while troll.health > 0 or user_character.health > 0:
    print(f'-------------------- Round:{fight_round} --------------------')
    print(f'Moves:')
    print(f'{user_character.attack[0]}')

