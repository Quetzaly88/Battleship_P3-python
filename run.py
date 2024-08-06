import random

class TableGame:
    def __init__(self):
        """
        Start the board with a dictionary with tuples (x,y). 
        use cero as empty spot. 
        """
        self.grid = {(x, y): "0" for x in range(5) for y in range(5)} #grid attribute represents dictionary