from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image

from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.graphics import Rectangle, Ellipse, Line

NOTEXTURE = "assets/NOTEXTURE.png"
CURSOR = "assets/CURSOR.png"

class StartScreen(Widget):
    def __init__(self):
        super(StartScreen, self).__init__()
        self.layout = FloatLayout()
        self.add_widget(self.layout)
        #Creating Widgets
        self.background = Image(
            width = Window.width,
            height = Window.height,
            color=(255, 0, 0, 1)
        )
        self.startText = Label(
            text="Poodle Jump",
            width=300,
            height=75,
            center_x=Window.width / 2,
            center_y=Window.height / 2,
            font_size=50
        )
        self.startButton = Button(
            text="Start",
            width=300,
            height=75,
            center_x=Window.width / 2,
            center_y=Window.height / 2 - 100,
            font_size=32
        )
        self.settingsButton = Button(
            text="Settings",
            width=300,
            height=75,
            center_x=Window.width / 2,
            center_y=Window.height / 2 - 200,
            font_size=32
        )
        self.mouseTexture = Image(
            source=CURSOR,
            texture_size=(20, 20),
            size=(20, 20)
        )
        #Adding Widgets
        self.layout.add_widget(self.background)
        self.layout.add_widget(self.startText)
        self.layout.add_widget(self.startButton)
        self.layout.add_widget(self.settingsButton)
        self.layout.add_widget(self.mouseTexture)

        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def on_touch_move(self, *args):
        pass

    def update(self, *args):
        self.mouseTexture.center_x = Window.mouse_pos[0]
        self.mouseTexture.center_y = Window.mouse_pos[1]

        # self.canvas.after.clear()
        # self.startText.canvas.after.clear()
        # with self.canvas.after:
        #     Rectangle(pos=(Window.mouse_pos[0],
        #                    Window.mouse_pos[1]),
        #               size=(10,
        #                     10))