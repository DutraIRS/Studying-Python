class Warrior:
    def __init__(self, name):
        self.__name = name
        self.__armor = None
        self.__shield = None
        self.__weapons = []
        
    @property
    def name(self):
        return self.__name    
        
    @property
    def shield(self):
        return self.__shield
        
    @shield.setter
    def shield(self, shield):
        self.__shield = shield
    
    @property
    def weapons(self):
        for weapon in self.__weapons:
            print('This weapon has this damage:', weapon.damage)
    
    def equip_weapon(self, weapon):
        self.__weapons.append(weapon)
        
    def equip_armor(self, defense):
        self.__armor = Armor(defense)
        
    def __del__(self):
        # del self.__armor # this makes the armor destroy itself right before the warrior dies
        print(f'{self.name} has been defeated. Your journey ends here.')
    
class Armor:
    def __init__(self, defense):
        self.__defense = defense
        
    def __del__(self):
        print(f'Armor with defense {self.__defense} has been destroyed.')

class Shield:
    def block(self):
        print('You have blocked the attack.')
        
class Sword:
    def __init__(self, damage):
        self.__damage = damage
        
    @property
    def damage(self):
        return self.__damage
    
    def attack(self):
        print('You have caused {damage} damage points to the enemy.'.format(damage = self.__damage))