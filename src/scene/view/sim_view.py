import arcade
import arcade.gui

from core import World, Mouse


class View(arcade.View):
    def __init__(self, window=None):
        # engine
        self.world = World()
        self.mouse = Mouse()

        # display setup
        arcade.load_font(r"C:\Data\suns\asset\font\digital-7 (mono).ttf")

        # display sprite
        self.background_color = arcade.color.DARK_BLUE_GRAY
        self.court_sprite: arcade.Sprite = self.world.init_court()
        self.player_sprite_list = arcade.SpriteList()
        self.rim_sprite: arcade.Sprite = self.world.init_rim()
        self.shotclock_sprite: arcade.Sprite = self.world.init_shotclock()

        # gui
        self.gui_manager = arcade.gui.UIManager(window)

        super().__init__(window, self.background_color)

    """----------- communicate -------------"""

    def add_player_event(self):
        pass

    """----------- visual -------------"""

    def on_draw(self):
        self.clear()

        arcade.draw_sprite(self.court_sprite)
        self.player_sprite_list.draw()
        for player_sprite in self.player_sprite_list:
            player_sprite.draw_text()
        arcade.draw_sprite(self.rim_sprite)
        arcade.draw_sprite(self.shotclock_sprite)
        self.shotclock_sprite.draw_text()
        self.gui_manager.draw()

    """----------- update view and world -------------"""

    def on_update(self, delta_time):
        # sync world
        self.world.update(delta_time)

        # event update
        self.mouse.update(delta_time)

        # display update
        self.court_sprite.update(delta_time)
        self.player_sprite_list.update(delta_time)
        self.rim_sprite.update(delta_time)
        self.shotclock_sprite.update(delta_time)

    """----------- sprite_event -------------"""

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def on_mouse_drag(self, x, y, dx, dy, _buttons, _modifiers):
        pass

    def on_mouse_release(self, x, y, button, modifiers):
        pass

    def on_mouse_motion(self, x, y, dx, dy):
        pass
