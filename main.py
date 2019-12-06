# -*- coding: utf-8 -*-

from automates.langton import LangtonAnt

if __name__ == '__main__':

    langton = LangtonAnt(100, 100)
    langton.initialize()

    for i in range(1000):
        langton.evolves()
        langton.saveImg(filepath="output/langton.%.03d.png" % (langton.step + 1))
