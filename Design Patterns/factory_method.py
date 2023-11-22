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
    @staticmethod
    @abstractmethod
    def get_chair(type_: str) -> Chair: ...

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
possible_chairs_ikea.append(IKEAChairFactory.get_chair("arm_chair"))
possible_chairs_ikea.append(IKEAChairFactory.get_chair("folding_chair"))
possible_chairs_ikea.append(IKEAChairFactory.get_chair("beanbag_chair"))
possible_chairs_ikea.append(IKEAChairFactory.get_chair("rocking_chair"))

for chair in possible_chairs_ikea:
    chair.sit()

possible_chairs_hni = []
possible_chairs_hni.append(HNIChairFactory.get_chair("arm_chair"))
possible_chairs_hni.append(HNIChairFactory.get_chair("rocking_chair"))

for chair in possible_chairs_hni:
    chair.sit()