import sys
import random


class TableGame:
    def __init__(self):
        self.grid = {(x, y): "*" for x in range(5) for y in 'ABCDE'}
        self.ships = []
        self.guesses = []

    def display_board(self, hide_ships=False):
        rows = ["   A B C D E"]
        for x in range(5):
            row = [f"{x} |"]
            for y in 'ABCDE':
                val = self.grid[(x, y)]
                if hide_ships and val == 'S':
                    val = "*"
                row.append(val)
            rows.append(" ".join(row))
        print("\n" + "\n".join(rows) + "\n")

    def place_ship(self, x, y):
        self.grid[(x, y)] = 'S'
        self.ships.append((x, y))

    def make_move(self, x, y):
        if self.grid[(x, y)] == 'S':
            print("HIT!")
            self.grid[(x, y)] = 'X'
            self.ships.remove((x, y))
            return True
        else:
            print("MISS!")
            self.grid[(x, y)] = '-'
            return False


def get_input(prompt):
    print(prompt, end='', flush=True)
    value = sys.stdin.readline()
    if not value:
        return ""
    return value.strip()


def ask_user_position():
    while True:
        try:
            full_input = get_input("Enter your guess (e.g., 2B) or type 'exit': ").strip().upper()
            
            if full_input.lower() == 'exit':
                print("Game exited. Goodbye!")
                sys.exit()
            
            if not full_input:
                print("Input cannot be empty. Try again.")
                continue

            if len(full_input) != 2:
                raise ValueError("Input must be 2 characters long (e.g., 2B).")
            
            if not full_input[0].isdigit() or full_input[1] not in 'ABCDE':
                raise ValueError("Row must be 0–4 and column must be A–E.")

            row = int(full_input[0])
            col = full_input[1]
            return row, col

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

    print("\nBattleship ultimate!\n")
    rounds = 10

# Main gameplay loop
    while rounds > 0:
        print(f"-- Round {11 - rounds} --\n")
        print("Your board:")
        user_board.display_board()

        print("Computer's board (hidden ships):")
        computer_board.display_board(hide_ships=True)

        # User move
        print("Your turn:")
        while True:
            row_number, column_letter = ask_user_position()

            if (row_number, column_letter) not in computer_board.grid:
                print("Invalid position. Try again.")
                continue

            if computer_board.grid[(row_number, column_letter)] in ['X', '-']:
                print("You've already guessed this spot. Try again.")
            else:
                break
        
        if computer_board.make_move(row_number, column_letter):
            if not computer_board.ships:
                print("You've sunk all the ships! You win!")
                break

        # Computer's turn
        print("\nComputer's turn:")
        comp_row, comp_col = computer_guess(user_board.guesses)
        print(f"Computer guessed: {comp_row}, {comp_col}")

        if user_board.make_move(comp_row, comp_col):
            if not user_board.ships:
                print("\nAll your ships have been sunk! You lose!")
                break

        rounds -= 1

        if rounds == 0:
            print("\nNo more rounds left. Game over!")
            if len(user_board.ships) > len(computer_board.ships):
                print("You win by having more ships left!")
            elif len(computer_board.ships) > len(user_board.ships):
                print("The computer wins with more ships left!")
            else:
                print("It's a tie! Both players have the same number of ships!")
            break

    # Show the final boards
    print("Final boards:")
    print("Your board:")
    user_board.display_board()
    print("Computer's board (Final State):")
    computer_board.display_board()


if __name__ == "__main__":
    main()
