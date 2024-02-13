import random

class SudokuGame:
    def __init__(self):
        self.board = self.generate_random_board()
        self.user_scores = {}

    def generate_random_board(self):
        # Create an empty 9x9 board
        empty_board = [[0] * 9 for _ in range(9)]

        # Fill the board with a random Sudoku solution
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(numbers)

        for i in range(9):
            empty_board[i][i] = numbers[i]

        # Shuffle rows and columns to create a valid Sudoku solution
        random.shuffle(empty_board)
        for row in empty_board:
            random.shuffle(row)

        return empty_board


    def display_board(self):
        horizontal_line = "+-------+-------+-------+"
        print(horizontal_line)
        for i, row in enumerate(self.board):
            if i % 3 == 0 and i != 0:
                print(horizontal_line)
            row_str = "| " + " ".join(map(str, row[:3])) + " | " + " ".join(map(str, row[3:6])) + " | " + " ".join(map(str, row[6:])) + " |"
            print(row_str)
        print(horizontal_line)


    def login(self):
        username = input("Enter your username: ")
        print(f"Welcome, {username}! You are now logged in.")


    def calculate_score(self):
        score = sum(row.count(0) for row in self.board)
        return score


    def play_game(self):
        print("\nLet's play Sudoku!")
        self.display_board()

        # Create a copy of the original board to keep track of the pre-generated numbers
        original_board = [row[:] for row in self.board]

        while True:
            row = int(input("Enter row number (1-9): ")) - 1
            col = int(input("Enter column number (1-9): ")) - 1

            # Check if the selected cell contains a pre-generated number
            if original_board[row][col] != 0:
                print("You cannot edit this cell. Please choose a different cell.")
                continue

            value = int(input("Enter value (1-9): "))

            # Update the board only if the cell is not a pre-generated number
            if original_board[row][col] == 0:
                self.board[row][col] = value

            self.display_board()

            if all(all(cell != 0 for cell in row) for row in self.board):
                print("Congratulations! You completed the Sudoku puzzle.")
                break

            go_back = input("Do you want to go back to the main menu? (yes/no): ")
            if go_back.lower() == "yes":
                return

        score = self.calculate_score()
        print(f"Your score: {score}")

        go_back = input("Do you want to go back to the main menu? (yes/no): ")
        if go_back.lower() == "yes":
            return



    def play_sandbox_game(self):
        while True:
            print("\nLet's play Sudoku!")
            self.display_board()

            while True:
                row = int(input("Enter row number (1-9): ")) - 1
                col = int(input("Enter column number (1-9): ")) - 1
                value = int(input("Enter value (1-9): "))

                self.board[row][col] = value

                self.display_board()

                if all(all(cell != 0 for cell in row) for row in self.board):
                    print("Congratulations! You completed the Sudoku puzzle.")
                    break

                go_back = input("Do you want to go back to the main menu? (yes/no): ")
                if go_back.lower() == "yes":
                    return

            score = self.calculate_score()
            print(f"Your score: {score}")

            go_back = input("Do you want to go back to the main menu? (yes/no): ")
            if go_back.lower() == "yes":
                return

    def intial_prompts(self):
        while True:
            print("\nMenu:")
            print("1. Play")
            print("2. Highscores")
            print("3. Instructions")
            print("4. Sandbox")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.play_game()
            elif choice == "2":
                print("Highscores:")
                for user, score in self.user_scores.items():
                    print(f"{user}: {score}")
            elif choice == "3":
                print("How to play Sudoku: A 9×9 square must be filled in with numbers from 1-9 with no repeated numbers in each line, horizontally or vertically. If you are able to accomplish this, then you win!")
            elif choice == "4":
                print("Sandbox: Enjoy solving Sudoku without scoring.")
                self.play_sandbox_game()
            elif choice == "5":
                print("Exiting the game. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")


    def start_program(self):
        self.login()
        self.intial_prompts()

if __name__ == "__main__":
    sudoku_game = SudokuGame()
    sudoku_game.start_program()
