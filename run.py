

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
    """
    Create board for two users. A person and the computer. Generate
    random positions ensuring to not have duplicates. Use loops.
    and a range from 1-5. 
    """
    tom_board = TableGame()
    computer_board = TableGame()
    
    # On Tom's board, randint() method to return a random integer between(parameter).
    for _ in range(5):
        while True:
            x, y = random.randint(0, 4), random.choice('ABCDE')
            # no duplicate positions
            if (x, y) not in tom_board:
                tom_board.place_ship(x, y)
                break

    # On computer's board, randint() method to return a random integer between(parameter).
    for _ in range(5):
        while True:
            x, y = random.randint(0, 4), random.choice('ABCDE')
            # no duplicate positions
            if (x, y) not in computer_board:
                computer_board.place_ship(x, y)
                break
    
    print("Battleship ultimate!")
    #initiate counting guesses
    guesses = 0

    # Loop until the player makes correct guesses. Allowed 5 turns. 
    while guesses < 5:
        print("You are Tom. This is your board:")
        tom_board.display_board()
        # computer's board has hidden ships. 
        print("Computer's board:")
        computer_board.hide_ships()

        # users guess
        print("Take your chance and guess where is a battleship")

        # new variables 
        row_number, column_letter = ask_user_position()

        # check if position is already taken 
        if computer_board.grid[(row_number, column_letter)] in ['X', '-']:
            print("That place is taken")
            # another guess
            continue

        if computer_board.make_move[(row_number, column_letter)]:
            guesses += 1
            


        
