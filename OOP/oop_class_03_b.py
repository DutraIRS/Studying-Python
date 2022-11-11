from oop_class_03_a import Warrior
from oop_class_03_a import Armor
from oop_class_03_a import Shield
from oop_class_03_a import Sword
from oop_class_03_a import Weapon
from oop_class_03_a import Axe

warrior_a = Warrior('Conan the Barbarian')
print(warrior_a)
#print(warrior_a.__name)
shield_a = Shield()

warrior_a.shield = shield_a

print(warrior_a.name)
warrior_a.shield.block()

sword_a = Sword(100, 'Excalibur')
print(sword_a.damage)
sword_b = Sword(1000)
print(sword_b.damage)

sword_a.attack()
sword_b.attack()

warrior_a.equip_weapon(sword_a)
warrior_a.equip_weapon(sword_b)

warrior_a.weapons

armor_a = Armor(50)
del armor_a

warrior_a.equip_armor(100)
print(warrior_a._Warrior__armor._Armor__defense) # this is so wrong
del warrior_a

print('\n:)\n'*2)

axe_a = Axe(500, 'Baruk Khazad', 10)
warrior_b = Warrior('Pangu the Great')
warrior_b.equip_weapon(axe_a)
warrior_b.equip_weapon(sword_a)
warrior_b.test_weapons()
axe_a.attack

print('program end')