from abc import ABC, abstractmethod
from typing import List, Dict, Tuple

# Client
# Invoker
# Command
# Receiver

# Receiver
class SmartLight:
    def __init__(self, name: str, location: str) -> None:
        self.name = name
        self.location = location
        self.state = False
        self.color = (255, 255, 255)

    def turn_on(self) -> None:
        self.state = True
        print(f"{self.name} is on at {self.location}")

    def turn_off(self) -> None:
        self.state = False
        print(f"{self.name} is off at {self.location}")

    def change_color(self, color: Tuple[int, int, int]) -> None:
        if self.state:
            self.color = color
            print(f"{self.name} is now {color} at {self.location}")
        else:
            print(f"{self.name} is off at {self.location}")

# Command
class ICommand(ABC):
    @abstractmethod
    def execute(self) -> None: ...

    @abstractmethod
    def undo(self) -> None: ...

# Concrete Command
class LightSwitchCommand(ICommand):
    def __init__(self, light: SmartLight) -> None:
        self.light = light

    def execute(self) -> None:
        if self.light.state:
            self.light.turn_off()
        else:
            self.light.turn_on()

    def undo(self) -> None:
        self.execute()

# Concrete Command
class LightColorChangeCommand(ICommand):
    def __init__(self, light: SmartLight, color: Tuple[int, int, int]) -> None:
        self.light = light
        self.color = color
        self._old_color = self.light.color

    def execute(self) -> None:
        self._old_color = self.light.color
        self.light.change_color(self.color)

    def undo(self) -> None:
        self.light.change_color(self._old_color)

# Invoker
class Alexa:
    def __init__(self) -> None:
        self._commands: Dict[str, ICommand] = {}
        self._commad_history: List[Tuple[str, str]] = []

    def add_command(self, name: str, command: ICommand) -> None:
        self._commands[name] = command

    def execute_command(self, name: str) -> None:
        if name in self._commands:
            self._commands[name].execute()
            self._commad_history.append((name, "execute"))
        else:
            print(f"Command {name} not found")

    def undo_command(self) -> None:
        if len(self._commad_history) > 0:
            name, action = self._commad_history.pop()
            if name in self._commands:
                if action == "execute":
                    self._commands[name].undo()
                    self._commad_history.append((name, "undo"))
                else:
                    self._commands[name].execute()
                    self._commad_history.append((name, "execute"))
            else:
                print(f"Command {name} not found")
        else:
            print("No commands to undo")

    def view_command_history(self) -> None:
        if len(self._commad_history) > 0:
            print("Command History:")
            for name, action in self._commad_history[::-1]:
                print(f"\t{name} {action}")
        else:
            print("No commands executed")

living_room_light = SmartLight("Philips Hue Candle", "Living Room")
dining_room_light = SmartLight("Philips Hue Slim", "Dining Room")

living_room_light_switch = LightSwitchCommand(living_room_light)
dining_room_light_switch = LightSwitchCommand(dining_room_light)

dining_room_light_change_color_blue = LightColorChangeCommand(dining_room_light, (0, 0, 255))
dining_room_light_change_color_red = LightColorChangeCommand(dining_room_light, (255, 0, 0))
dining_room_light_switch_color_green = LightColorChangeCommand(dining_room_light, (0, 255, 0))

virtual_assistant = Alexa()
virtual_assistant.add_command("living_room_light_switch", living_room_light_switch)
virtual_assistant.add_command("dining_room_light_switch", dining_room_light_switch)
virtual_assistant.add_command("dining_room_light_change_color_blue", dining_room_light_change_color_blue)
virtual_assistant.add_command("dining_room_light_change_color_red", dining_room_light_change_color_red)
virtual_assistant.add_command("dining_room_light_switch_color_green", dining_room_light_switch_color_green)

virtual_assistant.execute_command("dining_room_light_change_color_blue")
virtual_assistant.execute_command("dining_room_light_switch")
virtual_assistant.execute_command("dining_room_light_change_color_blue")
virtual_assistant.undo_command()
virtual_assistant.undo_command()
virtual_assistant.view_command_history()
