import math


def rotate90Right(i, j):
    dAngle = math.acos(i) if j > 0 else - math.acos(i)
    dAngle -= math.pi / 2
    return int(math.cos(dAngle)), int(math.sin(dAngle))


def rotate90Left(i, j):
    dAngle = math.acos(i) if j > 0 else - math.acos(i)
    dAngle += math.pi / 2
    return int(math.cos(dAngle)), int(math.sin(dAngle))


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
