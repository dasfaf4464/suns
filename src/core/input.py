class Mouse:
    def __init__(self):
        self.is_pressed = False
        self.press_time = 0.0
        self.hover_time = 0.0
        self.pressed_target = None
        self.hovered_target = None

    def on_left_click(self, sprite, callback, **kwargs):
        self.is_pressed = True

    def on_left_leave(self, sprite, callback, **kwargs):
        self.is_pressed = False

    def on_right_click(self, sprite):
        self.is_pressed = True
    
    def on_right_leave(self, sprite):
        self.is_pressed = False

    def on_hover(self, sprite):
        self.hovered_target = sprite

    def on_drag_left(self, sprite):
        
        pass

    def on_drag_right(self, sprite):
        pass

    def update(self, delta_time):
        pass