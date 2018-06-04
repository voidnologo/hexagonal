from collections import namedtuple
from decimal import Decimal
import math

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics.vertex_instructions import Line
# from kivy.graphics.context_instructions import Color


Point = namedtuple('Point', ['x', 'y'])

sin = {
    0: Decimal('0'),
    60: Decimal('0.866025403784439'),
    120: Decimal('0.866025403784439'),
    180: Decimal('0'),
    240: Decimal('-0.866025403784439'),
    300: Decimal('-0.866025403784439'),
}

cos = {
    0: Decimal('1'),
    60: Decimal('0.5'),
    120: Decimal('-0.5'),
    180: Decimal('-1'),
    240: Decimal('-0.5'),
    300: Decimal('0.5'),
}


def hex_corner(center, size, i):
    angle_deg = 60 * i
    return Point(center.x + size * cos[angle_deg],
                 center.y + size * sin[angle_deg])


def make_hex(center, size):
    vals = []
    for corner in range(6):
        corner = hex_corner(center, size, corner)
        vals.append(corner.x)
        vals.append(corner.y)
    return vals


class MyWidget(FloatLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = Window.size
        hex_size = 100

        with self.canvas:
            center = Point(Decimal(self.center_x), Decimal(self.center_y))
            self.draw_hex(center, hex_size)
            print(center)
            # self.draw_hex(Point(center.x + 2 * hex_size, center.y), hex_size)
            # self.draw_hex(Point(center.x - 2 * hex_size, center.y), hex_size)
            adjacent_x = Decimal(hex_size * 2 * 0.75)
            adjacent_y = Decimal((math.sqrt(3) / 2) * hex_size)
            print(adjacent_x)
            print(adjacent_y)
            # N
            self.draw_hex(Point(center.x, Decimal(center.y + (2 * adjacent_y))), hex_size)
            # NE
            self.draw_hex(Point(Decimal(center.x + adjacent_x), Decimal(center.y + adjacent_y)), hex_size)
            # SE
            self.draw_hex(Point(Decimal(center.x + adjacent_x), Decimal(center.y - adjacent_y)), hex_size)
            # S
            self.draw_hex(Point(center.x, Decimal(center.y - (2 * adjacent_y))), hex_size)
            # SW
            self.draw_hex(Point(Decimal(center.x - adjacent_x), Decimal(center.y + adjacent_y)), hex_size)
            # NW
            self.draw_hex(Point(Decimal(center.x - adjacent_x), Decimal(center.y - adjacent_y)), hex_size)

    def draw_hex(self, center, size):
        Line(points=make_hex(center, size), close=True, width=3)


class HexApp(App):

    def build(self):
        return MyWidget()


if __name__ == '__main__':
    HexApp().run()


# https://groups.google.com/forum/#!topic/kivy-users/nb77BpCWl2U
# https://stackoverflow.com/questions/20460965/centering-an-object-in-kivy
