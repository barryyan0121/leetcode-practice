"""2658. 网格图中鱼的最大数目"""


class Solution:
    def findMaxFish(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        answer = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    continue
                stack = [(i, j)]
                total = 0
                while stack:
                    x, y = stack.pop()
                    if not (0 <= x < rows and 0 <= y < cols) or grid[x][y] == 0:
                        continue
                    total += grid[x][y]
                    grid[x][y] = 0
                    stack.extend(((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)))
                answer = max(answer, total)
        return answer


if __name__ == "__main__":
    assert (
        Solution().findMaxFish([[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]])
        == 7
    )
