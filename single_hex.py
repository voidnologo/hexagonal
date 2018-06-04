from collections import namedtuple
from decimal import Decimal
import math

# STRIGHT FORWARD, but sin(180) is totally wrong due to floating point representation

Point = namedtuple('Point', ['x', 'y'])


def hex_corner(center, size, i):
    angle_rad = math.radians(60 * i)
    print('<>' * 10)
    print(i)
    print(angle_rad)
    print(math.cos(angle_rad))
    print(math.sin(angle_rad))
    return Point(center.x + size * math.cos(angle_rad),
                 center.y + size * math.sin(angle_rad))


center = Point(0, 0)
size = 5
for side in range(6):
    corner = hex_corner(center, size, side)
    print(f'Corner {side}: {corner}')


#  ====================================================================================================
print('<<<<>>>>'*10)

# Works correctly, but not as flexible

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


def enum_hex_corner(center, size, i):
    angle_deg = 60 * i
    print('<>' * 10)
    print(i)
    print(angle_deg)
    print(sin[angle_deg])
    print(cos[angle_deg])
    return Point(center.x + size * cos[angle_deg],
                 center.y + size * sin[angle_deg])


center = Point(0, 0)
size = 5
for side in range(6):
    corner = enum_hex_corner(center, size, side)
    print(f'Corner {side}: {corner}')
