
# cellular

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


## Output and convert to gif

```python
from cellular.samples.langton import LangtonAnt

automate = LangtonAnt(50, 50)
automate.initialize()

for _ in range(0, 200):
    automate.save_img(filepath="img/langton/langton.%.03d.png" % (automate.step))
    automate.evolves()
```

Then some ffmpeg : `ffmpeg -i img.%03d.png -vf scale=300:300 -sws_flags neighbor output.gif`

Langton simulation :
<img src="https://github.com/BastienLaby/cellular/blob/master/langton.gif" width="300">

Conway Game Of Life simulation :
<img src="https://github.com/BastienLaby/cellular/blob/master/conway.gif" width="300">
