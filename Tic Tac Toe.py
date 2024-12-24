import tkinter as tk  # Import the Tkinter module for GUI development
from tkinter import messagebox  # Import messagebox for displaying alerts


class TicTacToe:
    def __init__(self):
        # Initialize the main application window
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe Game")  # Set the window title
        self.window.geometry("450x600")  # Define the size of the window
        self.window.configure(bg="#282c34")  # Set the background color of the window
        self.window.resizable(False, False)  # Disable resizing of the window

        # Initialize game variables
        self.player = "X"  # Start with player "X"
        self.board = [" " for _ in range(9)]  # Create an empty 3x3 board as a list
        self.buttons = []  # List to store the button widgets
        self.x_score = 0  # Player X's score
        self.o_score = 0  # Player O's score

        # Create the GUI components
        self.create_dashboard()  # Add the title, scores, and reset button
        self.create_board()  # Create the 3x3 board
        self.update_scores()  # Display the initial scores

    def create_dashboard(self):
        """
        Sets up the game dashboard including title, player scores, and reset button.
        """
        # Create and display the game title
        self.title_label = tk.Label(
            self.window, text="Tic Tac Toe",  # Title text
            font=("Helvetica", 24, "bold"),  # Font style and size
            bg="#282c34", fg="#61dafb"  # Background and foreground colors
        )
        self.title_label.pack(pady=10)  # Add vertical padding around the label

        # Create and display the label for Player X's score
        self.x_label = tk.Label(
            self.window, text=f"Player X: {self.x_score}",  # Initial score for Player X
            font=("Helvetica", 14), bg="#282c34", fg="white"  # Styling
        )
        self.x_label.pack(pady=5)  # Add padding around the label

        # Create and display the label for Player O's score
        self.o_label = tk.Label(
            self.window, text=f"Player O: {self.o_score}",  # Initial score for Player O
            font=("Helvetica", 14), bg="#282c34", fg="white"  # Styling
        )
        self.o_label.pack(pady=5)  # Add padding around the label

        # Create and display the reset button
        self.reset_button = tk.Button(
            self.window, text="Reset Game",  # Button text
            font=("Helvetica", 14), bg="#61dafb", fg="black",  # Styling
            command=self.reset_game  # Function to call when the button is clicked
        )
        self.reset_button.pack(pady=10)  # Add padding around the button

    def create_board(self):
        """
        Creates the 3x3 game board with buttons for each cell.
        """
        # Create a frame to hold the buttons
        frame = tk.Frame(self.window, bg="#282c34")
        frame.pack(pady=20)  # Add padding around the frame

        # Create 9 buttons for the board
        for i in range(9):
            # Create a button with initial blank text
            btn = tk.Button(
                frame, text="", font=("Helvetica", 20, "bold"),  # Font style and size
                width=6, height=3,  # Button size
                bg="#61dafb", fg="black",  # Button colors
                command=lambda idx=i: self.make_move(idx)  # Assign the click handler
            )
            btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)  # Arrange buttons in a grid
            self.buttons.append(btn)  # Add the button to the list

    def make_move(self, idx):
        """
        Handles a player's move when they click a button.
        """
        if self.board[idx] == " ":  # Check if the cell is empty
            self.board[idx] = self.player  # Update the board with the current player's symbol
            # Update the button text and disable it
            self.buttons[idx].config(text=self.player, state=tk.DISABLED, disabledforeground="black")

            # Check if the current player has won
            if self.check_winner(self.player):
                self.declare_winner(self.player)  # Declare the winner
            elif " " not in self.board:  # Check if all cells are filled (a draw)
                messagebox.showinfo("Game Over", "It's a Draw!")  # Display a draw message
                self.reset_game()  # Reset the board
            else:
                # Switch to the other player
                self.player = "O" if self.player == "X" else "X"

    def check_winner(self, player):
        """
        Checks if the given player has won the game.
        """
        # Define the winning patterns (rows, columns, and diagonals)
        win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]
        # Check if any winning pattern is satisfied
        return any(all(self.board[i] == player for i in pattern) for pattern in win_patterns)

    def declare_winner(self, player):
        """
        Displays a message for the winner and updates the score.
        """
        messagebox.showinfo("Game Over", f"Player {player} wins!")  # Display winner message
        if player == "X":
            self.x_score += 1  # Increment Player X's score
        else:
            self.o_score += 1  # Increment Player O's score
        self.update_scores()  # Update the scores on the dashboard
        self.reset_game()  # Reset the game for a new round

    def update_scores(self):
        """
        Updates the score labels on the dashboard.
        """
        self.x_label.config(text=f"Player X: {self.x_score}")  # Update Player X's score label
        self.o_label.config(text=f"Player O: {self.o_score}")  # Update Player O's score label

    def reset_game(self):
        """
        Resets the game board and player turn.
        """
        self.board = [" " for _ in range(9)]  # Clear the board
        self.player = "X"  # Reset to Player X's turn
        for btn in self.buttons:
            btn.config(text="", state=tk.NORMAL)  # Clear and enable all buttons

    def run(self):
        """
        Starts the application's main loop.
        """
        self.window.mainloop()  # Start the Tkinter event loop


# Check if this script is run directly
if __name__ == "__main__":
    game = TicTacToe()  # Create a game instance
    game.run()  # Start the game
