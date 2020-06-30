# -*- coding: utf-8 -*-

import copy

from cellular.automate import Automate


_RELATIVE_NEIGHBORS = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
)


class ConwayGameOfLife(Automate):
    '''
    Automate wich reproduces the Conway's Game of Life (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).
    '''

    def evolves(self):
        '''
        Evolves following the rules of conway's game of life :
        * Any live cell with two or three neighbors survives.
        * Any dead cell with three live neighbors becomes a live cell.
        * All other live cells die in the next generation.
        '''

        current_gen = copy.deepcopy(self.grid)
        for i in range(self.width):
            for j in range(self.height):
                living_cell = current_gen[i][j]
                living_neighbors = 0
                for di, dj in _RELATIVE_NEIGHBORS:
                    try:
                        living_neighbors += 1 if current_gen[i + di][j + dj] else 0
                    except IndexError: # out of the grid
                        pass

                # Rule 3 : All other live cells die in the next generation.
                self.grid[i][j] = 0

                # Rule 1 : Any dead cell with three live neighbors becomes a live cell.
                if living_cell and living_neighbors in (2, 3):
                    self.grid[i][j] = 1

                # Rule 2 : Any dead cell with three live neighbors becomes a live cell.
                if not living_cell and living_neighbors == 3:
                    self.grid[i][j] = 1

        # increment the step

        self.step += 1
