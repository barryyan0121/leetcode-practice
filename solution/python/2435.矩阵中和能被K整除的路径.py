"""2435. 矩阵中和能被 K 整除的路径"""


class Solution:
    def numberOfPaths(self, grid: list[list[int]], k: int) -> int:
        mod = 10**9 + 7
        columns = len(grid[0])
        previous = [[0] * k for _ in range(columns)]
        for row, values in enumerate(grid):
            current = [[0] * k for _ in range(columns)]
            for column, value in enumerate(values):
                if row == column == 0:
                    current[0][value % k] = 1
                    continue
                for remainder in range(k):
                    if row:
                        current[column][(remainder + value) % k] += previous[column][
                            remainder
                        ]
                    if column:
                        current[column][(remainder + value) % k] += current[column - 1][
                            remainder
                        ]
                    current[column][(remainder + value) % k] %= mod
            previous = current
        return previous[-1][0]


if __name__ == "__main__":
    test_cases = [(([[5, 2, 4], [3, 0, 5], [0, 7, 2]], 3), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().numberOfPaths(*args) == expected
