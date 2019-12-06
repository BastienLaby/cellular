# -*- coding: utf-8 -*-

from automates.langton import LangtonAnt
from automates.conwayGameOfLife import ConwayGameOfLife

if __name__ == '__main__':

    ## Langton's app

    automate = LangtonAnt(100, 100)
    automate.initialize()

    for _ in range(0, 20):
        automate.saveImg(filepath="output/langton/langton.%.03d.png" % (automate.step))
        automate.evolves()

    ## Conway game of life

    automate = ConwayGameOfLife(100, 100)
    automate.initialize()

    # create blinker
    automate.grid[4][4] = 1
    automate.grid[4][5] = 1
    automate.grid[4][6] = 1

    # create pentadecathlon
    for i in range(8):
        automate.grid[10 + i][10] = 1
        automate.grid[10 + i][11] = 1
        automate.grid[10 + i][12] = 1
    automate.grid[11][11] = 0
    automate.grid[16][11] = 0

    for _ in range(30):
        automate.saveImg(filepath="output/conway/conway.%.03d.png" % (automate.step))
        automate.evolves()
