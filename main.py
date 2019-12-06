# -*- coding: utf-8 -*-

from automates import LangtonAnt

if __name__ == '__main__':

    langton = LangtonAnt(100, 100)
    langton.initialize()

    for i in range(1000):
        langton.evolve()
        langton.saveImg(filepath='langtong.%.03d.png' % i + 1)
