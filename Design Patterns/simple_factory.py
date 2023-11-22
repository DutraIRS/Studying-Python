# badly designed code
# class ArmChair:
#     def sit(self):
#         print("Sit on armchair")

# class FoldingChair:
#     def sit(self):
#         print("Sit on folding chair")

# class BeanBagChair:
#     def sit(self):
#         print("Sit on bean bag chair")

from abc import ABC, abstractmethod

class Chair(ABC):
    @abstractmethod
    def sit(self): ...

class ArmChair:
    def sit(self):
        print("Sit on armchair")

class FoldingChair:
    def sit(self):
        print("Sit on folding chair")

class BeanBagChair:
    def sit(self):
        print("Sit on bean bag chair")

class RockingChair:
    def sit(self):
        print("Sit on rocking chair")

class ChairFactory: # use enum
    @staticmethod
    def get_chair(type_: str) -> Chair:
        if type_ == "arm_chair":
            return ArmChair()
        elif type_ == "folding_chair":
            return FoldingChair()
        elif type_ == "beanbag_chair":
            return BeanBagChair()
        elif type_ == "rocking_chair":
            return RockingChair()
        else:
            raise ValueError(f"Chair of type {type_} not found")
        
# Driver code
possible_chairs = []
possible_chairs.append(ChairFactory.get_chair("arm_chair"))
possible_chairs.append(ChairFactory.get_chair("folding_chair"))
possible_chairs.append(ChairFactory.get_chair("beanbag_chair"))
possible_chairs.append(ChairFactory.get_chair("rocking_chair"))

for chair in possible_chairs:
    chair.sit()