# -*- coding: utf-8 -*-

import math

import automate


def rotateR(i, j):
    dAngle = math.acos(i) if j > 0 else - math.acos(i)
    dAngle -= math.pi / 2
    return int(math.cos(dAngle)), int(math.sin(dAngle))

def rotateL(i, j):
    dAngle = math.acos(i) if j > 0 else - math.acos(i)
    dAngle += math.pi / 2
    return int(math.cos(dAngle)), int(math.sin(dAngle))


class Point2D(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, tuple):
            return self.x == other[0] and self.y == other[1]
        elif isinstance(other, Point2D):
            return self.x == other.x and self.y == other.y

    def __str__(self):
        return '(%s %s)' % (self.x, self.y)

    def dirStr(self):
        if (self.x, self.y) == (0, 1): return '^'
        if (self.x, self.y) == (0, -1): return 'v'
        if (self.x, self.y) == (1, 0): return '>'
        if (self.x, self.y) == (-1, 0): return '<'


class Ant(object):
    def __init__(self, position, direction):
        self.pos = Point2D(position[0], position[1])
        self.dir = Point2D(direction[0], direction[1])


class LangtonAnt(automate.Automate):

    def __init__(self, width, height, name='langton'):
        automate.Automate.__init__(self, width=width, height=height, name=name)

    def initialize(self, antPosition=None, antDirection=None):
        super(LangtonAutomate, self).initialize()
        antPosition = antPosition or (self.width // 2, self.height // 2)
        antDirection = antDirection or (0, 1)
        self.ant = Ant(position=antPosition, direction=antDirection)

    def evolve(self):

        if self.grid[self.ant.pos.x][self.ant.pos.y]: # black
            self.ant.dir.x, self.ant.dir.y = rotateL(self.ant.dir.x, self.ant.dir.y)
        else: # white
            self.ant.dir.x, self.ant.dir.y = rotateR(self.ant.dir.x, self.ant.dir.y)

        self.grid[self.ant.pos.x][self.ant.pos.y] = int(not bool(self.grid[self.ant.pos.x][self.ant.pos.y]))

        self.ant.pos.x += self.ant.dir.x
        self.ant.pos.y += self.ant.dir.y

        self.step += 1

    def saveImgForData(self):
        '''
        '''
        self.imageData = []
        for j in range(self.height)[::-1]:
            row = []
            for i in range(self.width):
                if self.ant.pos == (i, j):
                    row += [255, 0, 0]
                elif self.grid[i][j]:
                    row += [255, 255, 255]
                else:
                    row += [0, 0, 0]
            self.imageData.append(row)
