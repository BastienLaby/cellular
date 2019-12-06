
# cellularAutomaton

Python API to create and display cellular automaton

## Dependencies

- [PyPNG](https://github.com/drj11/pypng) : `py 3.X -m pip install PyPNG`

## Description

Each cellular automaton derives from **Automate** class and has at least an **evolves()** method which describes how the system evolves in step N+1.
Example :

```python
# -*- coding: utf-8 -*-

from automates import LangtonAnt

if __name__ == '__main__':

    langton = LangtonAnt(100, 100) # grid size
    langton.initialize() # each subclass of Automate also override the initialize() method

    for i in range(1000):
        langton.evolve()
        langton.saveImg(filepath='langtong.%.03d.png' % langton.step + 1)
```

