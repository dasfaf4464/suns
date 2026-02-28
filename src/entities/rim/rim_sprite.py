import arcade


class RimSprite(arcade.Sprite):
    TEXTURE = arcade.load_texture(r"C:\Data\suns\asset\img\rim.png")

    def __init__(self, rim, center_x=0, center_y=0, angle=0, **kwargs):
        self.rim = rim
        super().__init__(
            RimSprite.TEXTURE, 0.145, center_x=796, center_y=362, angle=0, **kwargs
        )
        self.sync_hit_box_to_texture()
