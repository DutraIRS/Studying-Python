from abc import ABC, abstractmethod
from typing import List, Dict, Tuple

class IObserver(ABC):
    @abstractmethod
    def update(self) -> None: ...

class ISubject(ABC):
    @property
    @abstractmethod
    def state(self): ...

    @abstractmethod
    def add_observer(self, observer: IObserver) -> None: ...

    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None: ...

    @abstractmethod
    def notify_observers(self) -> None: ...

class CheatingDetector(ISubject):
    def __init__(self) -> None:
        self._observers: List[IObserver] = []
        self._state: Dict = {}

    @property
    def state(self) -> Dict:
        return self._state
    
    @state.setter
    def state(self, state_update: Dict) -> Dict:
        new_state: Dict = {**self._state, **state_update}

        if new_state != self._state:
            self._state = new_state
            self.notify_observers()
    
    def reset_state(self) -> None:
        self._state = {}
        self.notify_observers()

    def add_observer(self, observer: IObserver) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: IObserver) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update()

class ControlRoom(IObserver):
    def __init__(self, name, observable: ISubject) -> None:
        self.name = name
        self.observable = observable

    def update(self) -> None:
        observable_name = self.observable.__class__.__name__
        observable_state = self.observable.state

        print("#" * 42)
        print(f"{self.name}: \"{observable_name}\" has updated its state.")
        print(f"New state is {observable_state}.")

        if self.observable.state:
            print(f"Sending {self.observable.state} to the police.")

class MobileMonitor(IObserver):
    def __init__(self, name, observable: ISubject) -> None:
        self.name = name
        self.observable = observable

    def _detonate(self, observable_name: str) -> None:
        print(f"{self.name}: Preparing detonation at {observable_name}.")

    def update(self) -> None:
        observable_name = self.observable.__class__.__name__

        print("#" * 42)
        print(f"{self.name}: Something has happened.")
        print(f"Execute lockdown protocol at: {observable_name}.")

        self._detonate(observable_name)

cheating_detector_1 = CheatingDetector()

emap_control_room = ControlRoom("EMAP Control Room", cheating_detector_1)
nap_control_room = ControlRoom("NAP Control Room", cheating_detector_1)

president_mobile_monitor = MobileMonitor("President Mobile Monitor", cheating_detector_1)
director_mobile_monitor = MobileMonitor("Director Mobile Monitor", cheating_detector_1)

cheating_detector_1.add_observer(emap_control_room)
cheating_detector_1.add_observer(nap_control_room)
cheating_detector_1.add_observer(president_mobile_monitor)
cheating_detector_1.add_observer(director_mobile_monitor)

cheating_detector_1.state = {"Chair00": True}

cheating_detector_1.remove_observer(president_mobile_monitor)
cheating_detector_1.remove_observer(director_mobile_monitor)

cheating_detector_1.state = {"Chair15": True}