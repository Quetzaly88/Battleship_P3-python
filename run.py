import sys
import random


class TableGame:

    def __init__(self):
        """
        Start the board with a dictionary with tuples (x,y).
        X are numbers from 0-4 and y are letters A-E. Use * as empty spot.
        """
        self.grid = {(x, y): "*" for x in range(5) for y in 'ABCDE'}
        self.ships = []
        self.guesses = []

    def display_board(self, hide_ships=False):
        """
        Display the board with all elements (ships, hits, misses).
        """
        print(" A B C D E")
        for x in range(5):
            row = [str(x)]
            for y in 'ABCDE':
                cell = self.grid[(x, y)]
                row.append("*" if hide_ships and cell == 'S' else cell)
            print(" ".join(row))
        print()

    def place_ship(self, x, y):
        """
        Place a ship on the board and mark position with S,
        representing the Ship on the board.
        """
        self.grid[(x, y)] = 'S'
        self.ships.append((x, y))

    def make_move(self, x, y):
        """
        Processes a move: Hits ('X') or Misses ('-') a ship.
        """
        if self.grid[(x, y)] == 'S':
            print("HIT!")
            self.grid[(x, y)] = 'X'
            self.ships.remove((x, y))
            return True
        else:
            print("MISS!")
            self.grid[(x, y)] = '-'
            return False


def ask_user_position():
    """
    Ask user for position using input(). Integer for row and capital
    letter for column. Return the position as a Tuple. Return an
    error message if the input is not between the ones required.
    """
    if not sys.stdin.isatty():  # If running in Heroku or non-interactive terminal
        print("\nThis game requires user input. Please run it locally.")
        exit()

    while True:
        # urge the user for a valid input
        try:
            row_input = input("Enter row number (0 to 4) or type exit to quit: ").strip()
            if row_input.lower() == 'exit':
                print("Goodbye!")
                exit()

            col_input = input("Enter column letter (A to E): ").strip().upper()
            if col_input.lower() == 'exit':
                print("Goodbye!")
                exit()

            if not row_input.isdigit() or int(row_input) not in range(5) or col_input not in 'ABCDE':
                raise ValueError("Invalid input")

            return int(row_input), col_input

        except ValueError as e:
            print(f"Invalid input: {e}. Try again.\n")



def main():
    """
    Create board for two users. A person and the computer. Generate
    random positions ensuring to not have duplicates. Use loops.
    and a range from 1-5.
    """
    user_board = TableGame()
    computer_board = TableGame()

    # Place 5 ships on each board
    place_random_ships(user_board)
    place_random_ships(computer_board)

    print("Battleship ultimate!\n")
    rounds = 10

    for _ in range(5):
        while True:
            x, y = random.randint(0, 4), random.choice('ABCDE')
            if (x, y) not in tom_board.ships:
                tom_board.place_ship(x, y)
                break

    # Return a random integer between(parameter).
    for _ in range(5):
        while True:
            x, y = random.randint(0, 4), random.choice('ABCDE')
            if (x, y) not in computer_board.ships:
                computer_board.place_ship(x, y)
                break

    # Loop until the player makes correct guesses. Allowed 10 turns.
    while turns > 0:
        print("Welcome! This is your board:\n")
        tom_board.display_board()

        print("Computer's board:")
        computer_board.hide_ships()

        print("Take your chance and guess where is a battleship\n")

        row_number, column_letter = ask_user_position()

        if computer_board.grid[(row_number, column_letter)] in ['X', '-']:
            print("That place is taken")
            continue

        if computer_board.make_move(row_number, column_letter):
            if not computer_board.ships:
                print("You sunk all the ships!")
                break
        else:
            turns -= 1

        if turns == 0:
            print("You have no chances left!\n")

    print("Game Over")
    # print("Tom's board:")
    tom_board.display_board
    # print("computer's board:")
    computer_board.display_board()


if __name__ == "__main__":
    main()
