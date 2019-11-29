class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        def position(target: str) -> (int, int):
            board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
            for i, row in enumerate(board):
                for j, col in enumerate(row):
                    if col == target:
                        return i, j
        x_old = y_old = 0
        result = ""
        for char in target:
            y_new, x_new = position(char)
            x_distance = x_old - x_new
            y_distance = y_old - y_new
            if y_distance > 0:
                result += "U" * abs(y_distance)
            if x_distance < 0:
                result += "R" * abs(x_distance)
            if x_distance > 0:
                result += "L" * abs(x_distance)
            if y_distance < 0:
                result += "D" * abs(y_distance)
            result += "!"
            x_old, y_old = x_new, y_new
        return result