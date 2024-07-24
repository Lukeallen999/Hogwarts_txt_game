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
          