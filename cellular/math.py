import math


def rotate_90_right(i, j):
    delta_angle = math.acos(i) if j > 0 else - math.acos(i)
    delta_angle -= math.pi / 2
    return int(math.cos(delta_angle)), int(math.sin(delta_angle))


def rotate_90_left(i, j):
    delta_angle = math.acos(i) if j > 0 else - math.acos(i)
    delta_angle += math.pi / 2
    return int(math.cos(delta_angle)), int(math.sin(delta_angle))


class Vector2D(object):
    '''
    2D space representation
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, tuple):
            return self.x == other[0] and self.y == other[1]
        elif isinstance(other, Vector2D):
            return self.x == other.x and self.y == other.y
