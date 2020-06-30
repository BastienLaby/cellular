# -*- coding: utf-8 -*-

from cellular.automate import Automate
from cellular.math import Vector2D, rotate90Left, rotate90Right


class Ant(object):
    """
    Ant representation, with a position and a direction, each represented by a Vector2D.
    """

    def __init__(self, position, direction):
        self.pos = Vector2D(position[0], position[1])
        self.dir = Vector2D(direction[0], direction[1])


class LangtonAnt(Automate):
    """
    Automate wich reproduces the Langton's App behavior (https://en.wikipedia.org/wiki/Langton%27s_ant).
    """

    def __init__(self, width, height):
        Automate.__init__(self, width=width, height=height)
        self.ant = None

    def initialize(self, antPosition=None, antDirection=None):
        """
        Initialize the grid with a position and direction for the ant.
        """
        super(LangtonAnt, self).initialize()
        self.ant = Ant(
            antPosition or (self.width // 2, self.height // 2), antDirection or (0, 1)
        )

    def evolves(self):
        """
        Evolves following the rules of Langton's ant :
        * If the ant cell is white : rotate right, change the cell state, then move forward.
        * If the ant cell is black : rotate left, change the cell state, then move forward.
        """

        # rotate the ant

        if self.grid[self.ant.pos.x][self.ant.pos.y]:  # black
            self.ant.dir.x, self.ant.dir.y = rotate90Left(
                self.ant.dir.x, self.ant.dir.y
            )
        else:  # white
            self.ant.dir.x, self.ant.dir.y = rotate90Right(
                self.ant.dir.x, self.ant.dir.y
            )

        # set the cell position

        self.grid[self.ant.pos.x][self.ant.pos.y] = int(
            not bool(self.grid[self.ant.pos.x][self.ant.pos.y])
        )

        # move forward

        self.ant.pos.x += self.ant.dir.x
        self.ant.pos.y += self.ant.dir.y

        # increment the step

        self.step += 1

    def saveImgForData(self):
        """
        Same function as the default saveImgForData + ant cell is red.
        #TODO : call parent saveImgForData() function then just change the ant cell data.
        """
        self.imageData = []
        for j in range(self.height)[::-1]:
            row = []
            for i in range(self.width):
                if self.ant.pos == (i, j):
                    row += [255, 0, 0, 255]
                elif self.grid[i][j]:
                    row += [255, 255, 255, 255]
                else:
                    row += [0, 0, 0, 255]
            self.imageData.append(row)