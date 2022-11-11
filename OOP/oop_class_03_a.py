from abc import ABC, abstractmethod

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

    def test_weapons(self):
        for weapon in self.__weapons:
            weapon.attack()

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
        
class Weapon(ABC):
    def __init__(self, damage, name = None):
        self.__damage = damage
        self.__name = name
        
    @property
    def damage(self):
        return self.__damage

    @property
    def name(self):
        return self.__name
    
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        print(f'You swing your {self.__class__.__name__} {self.name} and cause {self.damage} to the enemy.')

class Axe(Weapon):
    def __init__(self, name, damage, range_length):
        super().__init__(name, damage)
        self.__range = range_length    

    @property
    def range(self):
        return self.__range

    def attack(self):
        print(f'You throw your {self.__class__.__name__} {self.name}, of range {self.range}, and cause {self.damage} to the enemy.')

    def knock_down_door(self):
        print(f'The {self.__class__.__name__} has been used to knock down the door.')