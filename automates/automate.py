# -*- coding: utf-8 -*-

import png # py -3.X -m pip install PyPNG


class Automate(object):
    '''
    Base Automate class. Cannot be used on his own because each subclass needs to implement the evolves() function.
    Each automate has :
    - a 2D grid
    - a "step" variable couting the number of evolutions
    - a "imageData" array variable containing the image data which represents the automate state.
    '''

    def __init__(self, width, height, name='automate'):
        self.width = width
        self.height = height
        self.grid = None
        self.step = 1
        self.imageData = None

    def initialize(self):
        '''
        By default, initialize a width * height grid with zeros values.
        '''
        self.grid = []
        for i in range(self.width):
            self.grid.append([])
            for j in range(self.height):
                self.grid[i].append(0)

    def evolves(self):
        '''
        Update the system by one step.
        This method has to be implemented in each subclass.
        '''
        raise NotImplementedError()

    def saveImgForData(self):
        '''
        Compute current grid data to create data image.
        '''
        self.imageData = []
        for j in range(self.height)[::-1]:
            row = []
            for i in range(self.width):
                if self.grid[i][j]:
                    row += [255, 255, 255, 255]
                else:
                    row += [0, 0, 0, 255]
            self.imageData.append(row)

    def saveImg(self, filepath=''):
        '''
        Save the image data to the given file.
        '''
        self.saveImgForData()
        writer = png.Writer(self.width, self.height, greyscale=False, alpha=True)
        with open(filepath, 'wb') as f:
            writer.write(f, self.imageData)
