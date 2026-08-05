"""3393. 统计异或值为给定值的路径数目"""


class Solution:
    def countPathsWithXorValue(self, grid: list[list[int]], k: int) -> int:
        mod = 10**9 + 7
        rows, columns = len(grid), len(grid[0])
        previous = [None] * columns
        for row in range(rows):
            current = [None] * columns
            for column in range(columns):
                counts = {}
                if row == 0 and column == 0:
                    counts[grid[0][0]] = 1
                else:
                    for source in (
                        previous[column] if row else {},
                        current[column - 1] if column else {},
                    ):
                        for value, count in source.items():
                            next_value = value ^ grid[row][column]
                            counts[next_value] = (
                                counts.get(next_value, 0) + count
                            ) % mod
                current[column] = counts
            previous = current
        return previous[-1].get(k, 0)


if __name__ == "__main__":
    test_cases = [(([[2, 1, 5], [7, 10, 0], [12, 6, 4]], 11), 3)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countPathsWithXorValue(*args) == expected
