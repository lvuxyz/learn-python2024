import tkinter as tk
from tkinter import messagebox

class Caro:
    def __init__(self, root):
        self.root = root
        self.root.title('Cờ Caro')
        self.current_player = 'X'
        self.board = [[None] * 3 for _ in range(3)]
        self.buttons = [[None] * 3 for _ in range(3)]
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text='', font=('Arial', 20), height=3, width=6,
                                   command=lambda row=i, col=j: self.on_click(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def on_click(self, row, col):
        if self.buttons[row][col]['text'] == '' and self.winner() is None:
            self.buttons[row][col]['text'] = self.current_player
            self.board[row][col] = self.current_player
            if self.winner():
                messagebox.showinfo('Chúc mừng', f'Người chơi {self.current_player} đã thắng!')
                self.reset_game()
            elif all(all(row) for row in self.board):
                messagebox.showinfo('Hòa', 'Trận đấu hòa!')
                self.reset_game()
            self.current_player = 'O' if self.current_player == 'X' else 'X'

    def winner(self):
        lines = []
        # Check rows and columns
        lines.extend(self.board)
        lines.extend([[self.board[i][j] for i in range(3)] for j in range(3)])
        # Check diagonals
        lines.append([self.board[i][i] for i in range(3)])
        lines.append([self.board[i][2-i] for i in range(3)])
        for line in lines:
            if line[0] == line[1] == line[2] and line[0] is not None:
                return line[0]
        return None

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ''
                self.board[i][j] = None

if __name__ == "__main__":
    root = tk.Tk()
    game = Caro(root)
    root.mainloop()
