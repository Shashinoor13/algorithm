import random

class NQueensLasVegas:
    def __init__(self, n):
        self.n = n
        self.solution = None
        self.find_solution()
        self.display_solution()

    def is_safe(self, board, row, col):
        for i in range(row):
            if (
                board[i] == col or
                board[i] - i == col - row or
                board[i] + i == col + row
            ):
                return False
        return True

    def find_solution(self):
        """Find a solution to the N-Queens problem using the Las Vegas approach."""
        while True:
            board = [-1] * self.n
            available_columns = list(range(self.n))

            for row in range(self.n):
                random.shuffle(available_columns)
                placed = False
                for col in available_columns:
                    if self.is_safe(board, row, col):
                        board[row] = col
                        placed = True
                        break
                if not placed:
                    break
            else:
                self.solution = board
                return

    def display_solution(self):
        """Display the solution in the console."""
        if not self.solution:
            print("No solution found.")
            return

        print(f"{self.n}-Queens Solution:")
        for row in range(self.n):
            line = [". " for _ in range(self.n)]
            line[self.solution[row]] = "Q "
            print("".join(line))

if __name__ == "__main__":
    N = 16
    NQueensLasVegas(N)
