from typing import Literal
from entities import (
    Player,
    PlayerSprite,
    Court,
    CourtSprite,
    Rim,
    RimSprite,
    Shotclock,
    ShotclockSprite,
)


class World:
    def __init__(self):
        self.player_list = []
        self.court = Court()
        self.shotclock = Shotclock()
        self.rim = Rim()

    def init_court(self):
        court_sprite = CourtSprite(self.court)
        return court_sprite
    
    def init_rim(self):
        rim_sprite = RimSprite(self.rim)
        return rim_sprite

    def init_shotclock(self):
        shotclock_sprite = ShotclockSprite(self.shotclock)
        return shotclock_sprite

    def add_player(self, x, y, side):
        player = Player(x, y, side)
        # set player
        player_sprite = PlayerSprite(player, x, y)
        self.player_list.append(player_sprite)

    def update(self, delta_time):
        self.shotclock.update(delta_time)