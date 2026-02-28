import arcade


class CourtSprite(arcade.Sprite):
    def __init__(self, court, **kwargs):
        # logical
        self.court = court

        # display
        texture = arcade.load_texture(
            r"C:\Data\suns\asset\img\basketball_court_right.png"
        )

        super().__init__(texture, 0.5, 450, 360, 0, **kwargs)
        self.sync_hit_box_to_texture()
    