from collections import namedtuple
import math

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Mesh, Color
# from kivy.graphics.context_instructions import Color


Point = namedtuple('Point', ['x', 'y'])

sin = {
    0: 0,
    60: 0.866025403784439,
    120: 0.866025403784439,
    180: 0,
    240: -0.866025403784439,
    300: -0.866025403784439,
}

cos = {
    0: 1,
    60: 0.5,
    120: -0.5,
    180: -1,
    240: -0.5,
    300: 0.5,
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
        vals.extend([0, 0])
    return vals


class MyWidget(FloatLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = Window.size
        hex_size = 100
        adjacent_x = hex_size * 2 * 0.75
        adjacent_y = math.sqrt(3) / 2 * hex_size

        with self.canvas:
            center = Point(self.center_x, self.center_y)
            Color(0, 0, 1)
            self.mesh = self.draw_mesh_hex(center, hex_size)
            # N
            Color(0, 1, 0)
            self.draw_mesh_hex(Point(center.x, center.y + (2 * adjacent_y)), hex_size)
            # NE
            Color(0, 1, 1)
            self.draw_mesh_hex(Point(center.x + adjacent_x, center.y + adjacent_y), hex_size)
            # SE
            Color(1, 0, 0)
            self.draw_mesh_hex(Point(center.x + adjacent_x, center.y - adjacent_y), hex_size)
            # S
            Color(1, 0, 1)
            self.draw_mesh_hex(Point(center.x, center.y - (2 * adjacent_y)), hex_size)
            # SW
            Color(1, 1, 0)
            self.draw_mesh_hex(Point(center.x - adjacent_x, center.y + adjacent_y), hex_size)
            # NW
            Color(1, 1, 1)
            self.draw_mesh_hex(Point(center.x - adjacent_x, center.y - adjacent_y), hex_size)

    def draw_mesh_hex(self, center, size):
        indices = [i for i in range(6)]
        vertices = make_hex(center, size)
        mode = 'triangle_fan'
        return Mesh(vertices=vertices, indices=indices, mode=mode)


class HexApp(App):

    def build(self):
        return MyWidget()


if __name__ == '__main__':
    HexApp().run()


# https://groups.google.com/forum/#!topic/kivy-users/nb77BpCWl2U
# https://stackoverflow.com/questions/20460965/centering-an-object-in-kivy

# MESH
# https://kivy.org/docs/examples/gen__canvas__mesh__py.html
