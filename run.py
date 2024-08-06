import random

class TableGame:
    def __init__(self):
        """
        Start the board with a dictionary with tuples (x,y). 
        X are numbers from 0-4 and y are letters A-E. Use * as empty spot. 
        """
        self.grid = {(x, y): "*" for x in range(5) for y in 'ABCDE'}
        # empty list
        self.ships = []

    
def main():
    #create board for two users. A person and the computer. 
    tom_board = TableGame()
    computer_board = TableGame()

    
