# -*- coding: utf-8 -*-

import png


class Automate(object):

    def __init__(self, width, height, name='automate'):
        self.width = width
        self.height = height
        self.grid = None
        self.step = 1
        self.imageData = None

    def initialize(self):
        '''
        By default, initialize a width * height gris with value of 0
        '''
        self.grid = []
        for i in range(self.width):
            self.grid.append([])
            for j in range(self.height):
                self.grid[i].append(0)

    def evolve(self):
        '''
        Update the system of one step.
        '''
        raise NotImplementedError()

    def saveImgForData(self):
        '''
        '''
        self.imageData = []
        for j in range(self.height)[::-1]:
            row = []
            for i in range(self.width):
                if self.grid[i][j]:
                    row += [255, 255, 255]
                else:
                    row += [0, 0, 0]
            self.imageData.append(row)

    def saveImg(self, filepath=''):
        self.saveImgForData()
        writer = png.Writer(self.width, self.height, greyscale=False)
        with open(filepath, 'wb') as f:
            writer.write(f, self.imageData)
