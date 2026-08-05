"""2510. 检查是否有路径经过相同数量的 0 和 1"""


class Solution:
    def isThereAPath(self, grid: list[list[int]]) -> bool:
        rows, columns = len(grid), len(grid[0])
        previous = [set() for _ in range(columns)]
        for row in range(rows):
            current = [set() for _ in range(columns)]
            for column in range(columns):
                value = 1 if grid[row][column] else -1
                if row == column == 0:
                    current[column].add(value)
                else:
                    if row:
                        current[column].update(
                            difference + value for difference in previous[column]
                        )
                    if column:
                        current[column].update(
                            difference + value for difference in current[column - 1]
                        )
            previous = current
        return 0 in previous[-1]


if __name__ == "__main__":
    test_cases = [
        (([[0, 1, 0, 0], [0, 1, 0, 0], [1, 0, 1, 0]],), True),
        (([[1, 1, 0], [0, 0, 1], [1, 0, 0]],), False),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().isThereAPath(*args) == expected
