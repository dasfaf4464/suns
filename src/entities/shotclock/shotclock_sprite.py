import arcade

class ShotclockSprite(arcade.Sprite):
    TEXTURE = arcade.load_texture(r"C:\Data\suns\asset\img\shotclock_background.png")

    def __init__(self, shotclock, center_x = 0, center_y = 0, **kwargs):
        # logical shotclock
        self.shotclock = shotclock

        #display
        self.text = ""
        self.text_display = arcade.Text(self.text, x=1090, y=665, anchor_x="center", anchor_y="center", font_name="Digital-7 Mono", font_size=46)

        super().__init__(ShotclockSprite.TEXTURE, scale=0.2, center_x=1090, center_y=665, angle=0, **kwargs)
        self.sync_hit_box_to_texture()
    
    def update(self, delta_time = 1 / 60, *args, **kwargs):
        time = self.shotclock.get_printable()
        self.text = f"{time:05.2f}"
        self.text_display.text = self.text

        if time <= 5:
            self.text_display.color = arcade.color.RED
        else:
            self.text_display.color = arcade.color.WHITE

    def draw_text(self):
        self.text_display.draw()