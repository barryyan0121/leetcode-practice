"""3248. 矩阵中的蛇"""


class Solution:
    def finalPositionOfSnake(self, n: int, commands: list[str]) -> int:
        row = 0
        col = 0
        directions = {
            "UP": (-1, 0),
            "RIGHT": (0, 1),
            "DOWN": (1, 0),
            "LEFT": (0, -1),
        }
        for command in commands:
            d_row, d_col = directions[command]
            row += d_row
            col += d_col
        return row * n + col


if __name__ == "__main__":
    test_cases = [
        ((2, ["RIGHT", "DOWN"]), 3),
        ((3, ["DOWN", "DOWN", "LEFT"]), 5),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().finalPositionOfSnake(*args) == expected
