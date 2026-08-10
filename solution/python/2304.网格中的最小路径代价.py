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
