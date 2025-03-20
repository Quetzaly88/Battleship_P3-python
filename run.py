import random
import sys


# class representing the game logic
class TableGame:
    def __init__(self):
        """
        Start the board with a dictionary with tuples (x,y).
        X are numbers from 0-4 and y are letters A-E. Use * as empty spot.
        """
        self.grid = {(x, y): "*" for x in range(5) for y in 'ABCDE'}
        self.ships = []  #list to store ship positions
        self.guesses = []  #track guesses to avoid repeats

    def display_board(self):
        """
        Display the board with all elements (ships, hits, misses).
        """
        print("  A B C D E")
        for x in range(5):
            row = [str(x)]
            for y in 'ABCDE':
                row.append(self.grid[(x, y)])
            print(" ".join(row))
        print()

    def place_ship(self, x, y):
        """
        Place a ship on the board and mark position with S,
        representing the Ship on the board.
        """
        self.grid[(x, y)] = 'S'
        self.ships.append((x, y))

    def hide_ships(self):
        """
        Display the board with ships hidden.
        Function used from display_board function.
        """
        print("  A B C D E")
        for x in range(5):
            row = [str(x)]
            for y in 'ABCDE':
                if self.grid[(x, y)] == 'S':
                    row.append("*")
                else:
                    row.append(self.grid[(x, y)])
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
    if not sys.stdin.isatty():  # if running in Heroku(non-interactive mode)
        print("\nThis game requires user input. Please run it locally")
        exit()
        
    while True:
        # urge the user for a valid input
        try:
            row_input = input("Enter row number (0 to 4) or type 'exit' to quit: ").strip()
            if row_input.lower() == 'exit':
                print("\nGame exited. Goodbye!")
                exit()

            col_input = input("Enter column letter (A-E): ").strip().upper()
            if col_input.lower() == 'exit':
                print("\nGame exited. Goodbye!")
                exit()

            # Check for empty input
            if not row_input or not col_input:
                raise ValueError("Both row and column inputs are required.")

            # Validate if the row is an integer
            if not row_input.isdigit():
                raise ValueError("Row must be a number between 0 and 4.")

            row = int(row_input)

            # Validate row and column range
            if row not in range(5) or col_input not in 'ABCDE':
                raise ValueError("Provide a valid column letter (A-E) and row number (0-4).")

            return row, col_input

        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.\n")


# function for the computer. Ensures new moves every time.
def computer_guess(previous_guesses):
    while True:
        x = random.randint(0, 4)
        y = random.choice('ABCDE')
        if (x, y) not in previous_guesses:
            return x, y


# Main game loop
def main():
    """
    Create board for two users. A person and the computer. Generate
    random positions ensuring to not have duplicates. Use loops.
    and a range from 1-5.
    """
    user_board = TableGame()
    computer_board = TableGame()

    # On user's board, method to return a random integer between(parameter).
    for _ in range(5):
        while True:
            x, y = random.randint(0, 4), random.choice('ABCDE')
            if (x, y) not in user_board.ships:
                user_board.place_ship(x, y)
                break

    # Place 5 ships randomly on the computer's board.
    for _ in range(5):
        while True:
            x, y = random.randint(0, 4), random.choice('ABCDE')
            if (x, y) not in computer_board.ships:
                computer_board.place_ship(x, y)
                break

    print("Battleship ultimate!\n")
    rounds = 10

    # Loop until the player makes correct guesses. Allowed 10 rounds.
    while rounds > 0:
        print(f"\n-- Round {11 - rounds} ---")
        print("Your board:")
        user_board.display_board()

        print("Computer's board:")
        computer_board.hide_ships()

        # User's turn
        print("Your turn to guess:\n")
        while True:
            row_number, column_letter = ask_user_position()

            # Check if position is free
            if computer_board.grid[(row_number, column_letter)] in ['X', '-']:
                print("That place is taken")
            else:
                break  #valid move
          
        # User's guess
        if computer_board.make_move(row_number, column_letter):
            if not computer_board.ships:
                print("You sunk all the ships!")
                break
        
        # Computer's turn
        print("Computer's turn:")
        comp_row, comp_col = computer_guess(user_board.guesses)
        user_board.guesses.append((comp_row, comp_col))  #record the guess

        print(f"Computer guessed: {comp_row}{comp_col}")
        if user_board.make_move(comp_row, comp_col):
            if not user_board.ships:
                print("The computer sunk all your ships.")
                break

        rounds -= 1

        if rounds == 0:
            print("\nGame over!")
            if len(user_board.ships) > len(computer_board.ships):
                print("You win by having more ships left!")
            elif len(computer_board.ships) > len(user_board.ships):
                print("The computer wins with more ships left!")
            else:
                print("It's a tie! Both players have the same number of ships!")
            break

    # Display the results

    print("Final Boards: ")
    print("Your Board: ")
    user_board.display_board()

    print("computer's board:")
    computer_board.display_board()

# Entry point of the program
if __name__ == "__main__":
    main()
