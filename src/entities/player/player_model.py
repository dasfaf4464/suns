from dataclasses import dataclass
from typing import Literal
from entities.player import Position, Side

@dataclass
class State:
    back_number: int | None = 99
    name: str | None = "TEST"
    position: Position | None = Position.TEST
    side: Side | None = None

@dataclass
class Action:
    x: int = 0
    y: int = 0
    direction_x:float = 0
    direction_y:float = 0
    has_ball: bool = False

class Player:
    def __init__(self, x, y, side):
        self.state = State(side=side)
        self.action = Action(x=x, y=y)

    def move_to(self, dx, dy, dt):
        pass

    def throw_ball(self, direction_x, direction_y, dt):
        pass

    def catch_ball(self):
        pass

    def get_printable(self, tag:Literal["name", "number", "position"]):
        if tag == "name":
            return self.state.name
        elif tag == "number":
            return str(self.state.back_number)
        elif tag == "position":
            return self.state.position
        
    def synchronize(self):
        pass