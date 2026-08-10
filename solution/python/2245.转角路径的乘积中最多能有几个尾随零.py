"""2245. 转角路径的乘积中最多能有几个尾随零"""


class Solution:
    def maxTrailingZeros(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        left = [[(0, 0) for _ in range(cols)] for _ in range(rows)]
        up = [[(0, 0) for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                value = grid[i][j]
                factors = (0, 0)
                while value % 2 == 0:
                    factors = (factors[0] + 1, factors[1])
                    value //= 2
                while value % 5 == 0:
                    factors = (factors[0], factors[1] + 1)
                    value //= 5
                left[i][j] = (
                    factors[0] + (left[i][j - 1][0] if j else 0),
                    factors[1] + (left[i][j - 1][1] if j else 0),
                )
                up[i][j] = (
                    factors[0] + (up[i - 1][j][0] if i else 0),
                    factors[1] + (up[i - 1][j][1] if i else 0),
                )
        right = [[(0, 0) for _ in range(cols)] for _ in range(rows)]
        down = [[(0, 0) for _ in range(cols)] for _ in range(rows)]
        answer = 0
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                value = grid[i][j]
                twos = fives = 0
                while value % 2 == 0:
                    twos += 1
                    value //= 2
                while value % 5 == 0:
                    fives += 1
                    value //= 5
                right[i][j] = (
                    twos + (right[i][j + 1][0] if j + 1 < cols else 0),
                    fives + (right[i][j + 1][1] if j + 1 < cols else 0),
                )
                down[i][j] = (
                    twos + (down[i + 1][j][0] if i + 1 < rows else 0),
                    fives + (down[i + 1][j][1] if i + 1 < rows else 0),
                )
                for a, b in (
                    (up[i][j], right[i][j]),
                    (up[i][j], left[i][j]),
                    (down[i][j], right[i][j]),
                    (down[i][j], left[i][j]),
                ):
                    answer = max(answer, min(a[0] + b[0] - twos, a[1] + b[1] - fives))
        return answer
