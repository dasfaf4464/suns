import arcade
from scene import View

if __name__ == "__main__":
    app = arcade.Window()
    view = View()

    app.run(view)