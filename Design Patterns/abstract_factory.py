from abc import ABC, abstractmethod

class Chair(ABC):
    @abstractmethod
    def sit(self): ...

class IKEAArmChair:
    def sit(self):
        print("Sit on armchair from IKEA")

class HNIArmChair:
    def sit(self):
        print("Sit on armchair from HNI")

class FoldingChair:
    def sit(self):
        print("Sit on folding chair")

class BeanBagChair:
    def sit(self):
        print("Sit on bean bag chair")

class RockingChair:
    def sit(self):
        print("Sit on rocking chair")

class ChairFactory(ABC): # use enum
    def __init__(self, type_):
        self.chair = self.get_chair(type_)

    @staticmethod
    @abstractmethod
    def get_chair(type_: str) -> Chair: ...

    def sit(self):
        self.chair.sit()

class IKEAChairFactory(ChairFactory):
    @staticmethod
    def get_chair(type_: str) -> Chair:
        if type_ == "arm_chair":
            return IKEAArmChair()
        elif type_ == "folding_chair":
            return FoldingChair()
        elif type_ == "beanbag_chair":
            return BeanBagChair()
        elif type_ == "rocking_chair":
            return RockingChair()
        else:
            raise ValueError(f"Chair of type {type_} not found")
        
class HNIChairFactory(ChairFactory):
    @staticmethod
    def get_chair(type_: str) -> Chair:
        if type_ == "arm_chair":
            return HNIArmChair()
        elif type_ == "rocking_chair":
            return RockingChair()
        else:
            raise ValueError(f"Chair of type {type_} not found")
        
# Driver code
possible_chairs_ikea = []
possible_chairs_ikea.append(IKEAChairFactory("arm_chair"))
possible_chairs_ikea.append(IKEAChairFactory("folding_chair"))
possible_chairs_ikea.append(IKEAChairFactory("beanbag_chair"))
possible_chairs_ikea.append(IKEAChairFactory("rocking_chair"))

for chair in possible_chairs_ikea:
    chair.sit()

possible_chairs_hni = []
possible_chairs_hni.append(HNIChairFactory("arm_chair"))
possible_chairs_hni.append(HNIChairFactory("rocking_chair"))

for chair in possible_chairs_hni:
    chair.sit()