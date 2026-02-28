from arcade.color import WHITE
from arcade.gui import UIGridLayout ,UILabel

class PlayerActionLabel(UILabel):
    def __init__(self, text = "", *, x = 0, y = 0, width = None, height = None, font_name=..., font_size = 12, text_color = arcade.color.WHITE, bold = False, italic=False, align="left", multiline = False, size_hint=..., size_hint_max=None, **kwargs):
        super().__init__(text, x=x, y=y, width=width, height=height, font_name=font_name, font_size=font_size, text_color=text_color, bold=bold, italic=italic, align=align, multiline=multiline, size_hint=size_hint, size_hint_max=size_hint_max, **kwargs)
        self.visible = False

    def on_event(self, event):
        return super().on_event(event)

class PlayerLayout(UIGridLayout):
    def __init__(self, *, x=0, y=0, width=1, height=1, children = ..., size_hint=..., size_hint_max=None, **kwargs):
        super().__init__(x=x, y=y, width=width, height=height, align_horizontal="center", align_vertical="center", children=children, size_hint=size_hint, size_hint_max=size_hint_max, horizontal_spacing=0, vertical_spacing=0, column_count=1, row_count=3, **kwargs)
        self.visible = False