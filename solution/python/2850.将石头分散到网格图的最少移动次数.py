"""2850. 将石头分散到网格图的最少移动次数"""

from itertools import permutations


class Solution:
    def minimumMoves(self, grid: list[list[int]]) -> int:
        extra, empty = [], []
        for row in range(3):
            for column in range(3):
                if grid[row][column] > 1:
                    extra.extend([(row, column)] * (grid[row][column] - 1))
                elif grid[row][column] == 0:
                    empty.append((row, column))
        return min(
            sum(abs(x - y) + abs(a - b) for (x, a), (y, b) in zip(extra, order))
            for order in permutations(empty)
        )


if __name__ == "__main__":
    assert Solution().minimumMoves([[1, 1, 0], [1, 1, 1], [1, 2, 1]]) == 3
