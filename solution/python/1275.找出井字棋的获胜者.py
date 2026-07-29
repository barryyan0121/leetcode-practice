from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        counts = [0] * 8
        for index, (row, col) in enumerate(moves):
            value = 1 if index % 2 == 0 else -1
            for line in (
                row,
                col + 3,
                6 if row == col else -1,
                7 if row + col == 2 else -1,
            ):
                if line >= 0:
                    counts[line] += value
                    if abs(counts[line]) == 3:
                        return "A" if value > 0 else "B"
        return "Draw" if len(moves) == 9 else "Pending"


if __name__ == "__main__":
    test_cases = [
        ([[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]], "A"),
        ([[0, 0], [1, 1]], "Pending"),
    ]
    for _, (moves, expected) in enumerate(test_cases):
        assert Solution().tictactoe(moves) == expected
