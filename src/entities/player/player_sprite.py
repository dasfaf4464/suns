import arcade
from entities.player import Side

class PlayerSprite(arcade.Sprite):
    OFF_TEXTURE = arcade.load_texture(r"C:\Data\suns\asset\img\blue_circle.png")
    DEF_TEXTURE = arcade.load_texture(r"C:\Data\suns\asset\img\red_circle.png")

    def __init__(self, player, center_x=0, center_y=0, **kwargs):
        # logical player
        self.player = player

        # display
        self.texture = None
        if player.state.side == Side.OFF:
            self.texture = PlayerSprite.OFF_TEXTURE
        elif player.state.side == Side.DEF:
            self.texture = PlayerSprite.DEF_TEXTURE
        self.scale = 1
        self.center_x = center_x
        self.center_y = center_y
        self.text = None
        self.text_display = arcade.Text("", x=0, y=0, anchor_x="center", anchor_y="center")

        super().__init__(self.texture, self.scale, center_x, center_y, 0, **kwargs)

    def update(self, delta_time=1 / 60, *args, **kwargs):
        pass

    def draw_text(self):
        if self.text:
            self.text_display.draw()