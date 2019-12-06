# -*- coding: utf-8 -*-

import copy

from automates import automate

relativeNeighors = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
)

class ConwayGameOfLife(automate.Automate):
    '''
    Automate wich reproduces the Conway's Game of Life (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).
    '''
    def __init__(self, width, height, name='conway'):
        automate.Automate.__init__(self, width=width, height=height, name=name)
        self.ant = None

    def evolves(self):
        '''
        Evolves following the rules of conway's game of life :
        * Any live cell with two or three neighbors survives.
        * Any dead cell with three live neighbors becomes a live cell.
        * All other live cells die in the next generation.
        '''

        currentGen = copy.deepcopy(self.grid)
        for i in range(self.width):
            for j in range(self.height):
                livingCell = currentGen[i][j]
                livingNeighbors = 0
                for dI, dJ in relativeNeighors:
                    try:
                        livingNeighbors += 1 if currentGen[i + dI][j + dJ] else 0
                    except IndexError: # out of the grid
                        pass

                # Rule 3 : All other live cells die in the next generation.
                self.grid[i][j] = 0

                # Rule 1 : Any dead cell with three live neighbors becomes a live cell.
                if livingCell and livingNeighbors in (2, 3):
                    self.grid[i][j] = 1

                # Rule 2 : Any dead cell with three live neighbors becomes a live cell.
                if not livingCell and livingNeighbors == 3:
                    self.grid[i][j] = 1

        # increment the step

        self.step += 1
