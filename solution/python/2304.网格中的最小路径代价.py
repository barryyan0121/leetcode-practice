"""2304. 网格中的最小路径代价"""


class Solution:
    def minPathCost(self, grid: list[list[int]], moveCost: list[list[int]]) -> int:
        dp = grid[0][:]
        for row in range(len(grid) - 1):
            nxt = [10**18] * len(grid[0])
            for column, cost in enumerate(dp):
                for next_column, next_value in enumerate(grid[row + 1]):
                    nxt[next_column] = min(
                        nxt[next_column],
                        cost + moveCost[grid[row][column]][next_column] + next_value,
                    )
            dp = nxt
        return min(dp)


if __name__ == "__main__":
    assert (
        Solution().minPathCost(
            [[5, 3], [4, 0], [2, 1]], [[9, 4], [6, 4], [1, 5], [7, 3], [2, 6], [8, 1]]
        )
        == 11
    )
