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
                # Hides ships unless specified
                if hide_ships and self.grid[(x, y)] == 'S':
                    row.append("*")
                else:
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


# Use readline instead of input() to receive data over socket stream
def get_input(prompt):
    print(prompt, end="", flush=True)
    return sys.stdin.readline().strip()


def ask_user_position():
    while True:
        try:
            row_input = get_input("Enter row number (0 to 4) or type exit to quit: ")
            if row_input.lower() == 'exit':
                print("Game exited. Goodbye!")
                sys.exit()

            col_input = get_input("Enter column letter (A to E): ").upper()
            if col_input.lower() == 'exit':
                print("Game exited. Goodbye!")
                sys.exit()

            if not row_input.isdigit() or int(row_input) not in range(5) or col_input not in 'ABCDE':
                raise ValueError("Provide a valid column letter (A-E) and row number (0-4).")

            return int(row_input), col_input

        except ValueError as e:
            print(f"Invalid input: {e}. Try again.\n")


def computer_guess(previous_guesses):
    while True:
        x = random.randint(0, 4)
        y = random.choice('ABCDE')
        if (x, y) not in previous_guesses:
            previous_guesses.append((x, y))
            return x, y


def main():
    user_board = TableGame()
    computer_board = TableGame()

    for _ in range(5):
        while True:
            x, y = random.randint(0, 4), random.choice('ABCDE')
            if (x, y) not in user_board.ships:
                user_board.place_ship(x, y)
                break

    for _ in range(5):
        while True:
            x, y = random.randint(0, 4), random.choice('ABCDE')
            if (x, y) not in computer_board.ships:
                computer_board.place_ship(x, y)
                break

    print("Battleship ultimate!\n")
    rounds = 10

# Main gameplay loop
    while rounds > 0:
        print(f"\n-- Round {11 - rounds} ---")
        print("Your board:")
        user_board.display_board()
        print("Computer's board (hidden ships):")
        computer_board.display_board(hide_ships=True)

        # User move
        print ("Your turn:")
        while True:
            row_number, column_letter = ask_user_position()
            if computer_board.grid[(row_number, column_letter)] in ['X', '-']:
                print("You've already guessed this spot. Try again.")
            else:
                break

        if computer_board.make_move(row_number, column_letter):
            if not computer_board.ships:
                print("You've sunk all the ships! You win!")
                break
        
        # Computer's turn
        print("Computer's turn:")
        comp_row, comp_col = computer_guess(user_board.guesses)
        print(f"Computer guessed: {comp_row}, {comp_col}")

        if user_board.make_move(comp_row, comp_col):
            if not user_board.ships:
                print("All your ships have been sunk! You lose!")
                break
        
        rounds -= 1

        if rounds == 0:
            print("No more rounds left. Game over!")
            if len(user_board.ships) > len(computer_board.ships):
                print("You win by having more ships left!")
            elif len(computer_board.ships) > len(user_board.ships):
                print("The computer wins with more ships left!")
            else:
                print("It's a tie! Both players have the same number of ships!")
            break

    # Show the final boards
    print("\nFinal boards:")
    print("Your board:")
    user_board.display_board()
    print("Computer's board (Final State):")
    computer_board.display_board()

if __name__ == "__main__":
    main()
