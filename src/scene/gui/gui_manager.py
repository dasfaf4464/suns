import arcade.gui

class UIManager(arcade.gui.UIManager):
    def __init__(self, window = None):
        self.panel = {}

        super().__init__(window)
        self.enable()

    
    