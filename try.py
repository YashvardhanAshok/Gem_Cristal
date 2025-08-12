import tkinter as tk
import random
from tkinter import messagebox

# Game settings
ROWS = 8
COLS = 8
MINES = 10
CELL_SIZE = 40

class Minesweeper:
    def __init__(self, root):
        self.root = root
        self.root.title("Minesweeper")

        self.buttons = {}
        self.mines = set()
        self.revealed = set()
        self.flags = set()

        self.create_widgets()
        self.place_mines()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack()

        for r in range(ROWS):
            for c in range(COLS):
                btn = tk.Button(frame, width=3, height=1, font=("Arial", 14, "bold"),
                                command=lambda r=r, c=c: self.reveal_cell(r, c))
                btn.bind("<Button-3>", lambda e, r=r, c=c: self.toggle_flag(r, c))
                btn.grid(row=r, column=c)
                self.buttons[(r, c)] = btn

    def place_mines(self):
        while len(self.mines) < MINES:
            r = random.randint(0, ROWS - 1)
            c = random.randint(0, COLS - 1)
            self.mines.add((r, c))

    def count_adjacent_mines(self, r, c):
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr, nc = r + dr, c + dc
                if (nr, nc) in self.mines and (dr != 0 or dc != 0):
                    count += 1
        return count

    def reveal_cell(self, r, c):
        if (r, c) in self.revealed or (r, c) in self.flags:
            return

        btn = self.buttons[(r, c)]
        self.revealed.add((r, c))

        if (r, c) in self.mines:
            btn.config(text="💣", bg="red", disabledforeground="black")
            self.game_over(False)
            return

        count = self.count_adjacent_mines(r, c)
        btn.config(text=str(count) if count > 0 else "", bg="lightgrey", relief=tk.SUNKEN)
        btn.config(state=tk.DISABLED)

        if count == 0:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS:
                        self.reveal_cell(nr, nc)

        if len(self.revealed) == ROWS * COLS - MINES:
            self.game_over(True)

    def toggle_flag(self, r, c):
        btn = self.buttons[(r, c)]
        if (r, c) in self.flags:
            btn.config(text="")
            self.flags.remove((r, c))
        elif (r, c) not in self.revealed:
            btn.config(text="🚩", fg="red")
            self.flags.add((r, c))

    def game_over(self, won):
        for (mr, mc) in self.mines:
            if (mr, mc) not in self.revealed:
                self.buttons[(mr, mc)].config(text="💣", bg="red")
        msg = "🎉 You Win!" if won else "💥 You hit a mine!"
        messagebox.showinfo("Game Over", msg)
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = Minesweeper(root)
    root.mainloop()
