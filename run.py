

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

        def display_board(self):
            """
            Display the board with all elements (ships, hits, misses).
            """
        # print column headers
        print(" A B C D E")
        # start row with the row number
        for x in range(5):
            row = [str(x)]
            for y in 'ABCDE':
                # show the value in the cell
                row.append(self.grid[(x, y)])
            # print the row
            print(" ".join(row))
        print()

    def place_ship(self, x, y):
        """
        Place a ship on the board and mark position with S,
        representing the Ship on the board.
        """
        self.grid[(x, y)] = 'S'
        # add the position and append it to list
        self.ships.append((x, y))

    def hide_ships(self):
        """
        Display the board with ships hidden.
        Function used from display_board function.
        """
        # print column headers
        print(" A B C D E")
        # start row with the row number
        for x in range(5):
            row = [str(x)]
            for y in 'ABCDE':
                if self.grid[(x, y)] == 'S':
                    row.append("*")
                else:
                    # show the value in the cell
                    row.append(self.grid[(x, y)])
            # print the row
            print(" ".join(row))
        print()

    def make_move(self, x, y):
        """
        Make a move using the two coordinates. If a ship is hit then
        use 'X'. If is a missmark with '-'.
        """
        if self.grid[(x, y)] == 'S':
            print("HIT!")
            self.grid[(x, y)] = 'X'
            return True
        else:
            print("MISS!")
            self.grid[(x, y)] = '-'
            return False

    def ask_user_position():
        """
        Ask user for position using input(). Integer for row and capital
        letter for column. Return the position as a Tuple. 
        """
        row = int(input("Enter row number. From 0 to 4"))
        col = input("Enter column letter. Use A-E").upper()
        return row, col 


def main():
    # reate board for two users. A person and the computer.
    tom_board = TableGame()
    computer_board = TableGame()

    print("Battleship ultimate!")