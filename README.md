
# cellularAutomaton

**cellular** is a Python API to create and display cellular automatons.
It provide a class `Automate` that you can derivate to create custom automatons.
The `Automate` class :
* Provides a `grid` variable to store the automate's data.
* Provides an `evolves()` method to override in order to describe how the system evolves at step N+1.

## Example

```python
import copy

from cellular.automate import Automate


class Blinker(Automate):
    """
    Automate that blink.
    """
    cell_data_type = bool

    def evolves(self):
        """
        Implement a blinker automate which inverse th state of every cell at each evolution.
        """
        current_gen = copy.deepcopy(self.grid)
        for i in range(self.width):
            for j in range(self.height):
                self.grid[i][j] = not current_gen[i][j]
        self.step += 1


blinker = Blinker(2, 2)
blinker.initialize()

blinker.grid[0][0] = False
blinker.grid[0][1] = True
blinker.grid[1][0] = True
blinker.grid[1][1] = False

for i in range(3):
    blinker.save_img(filepath="img/blinker/blinker.%.03d.png" % (blinker.step))
    blinker.evolves()
```


## Installation

* Clone this repository : `git clone <repo_url>`
* Create a virtualenv (I use Python 3.7 for this project) : `py -3.7 -m pip cellular`
* Move into the folder : `cd cellular`
* Activate the virtualenv : `.\Scripts\activate.bat` (windows) or `source bin/activate` (linux)
* Install the requirements : `pip install -r requirements.txt`

Done !


## Advanced usage

```python
from cellular.samples.langton import LangtonAnt
from cellular.samples.conway import ConwayGameOfLife


if __name__ == '__main__':

    ## Langton's app

    automate = LangtonAnt(100, 100)
    automate.initialize()

    for _ in range(0, 20):
        automate.save_img(filepath="img/langton/langton.%.03d.png" % (automate.step))
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
        automate.save_img(filepath="img/conway/conway.%.03d.png" % (automate.step))
        automate.evolves()
```

## Roadmap :

[ ] Use of NumPY for best performances

[ ] Custom cells states

[ ] YAML configuration for automate creations