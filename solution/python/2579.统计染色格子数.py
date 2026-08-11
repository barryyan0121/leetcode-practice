"""2579. 统计染色格子数"""


class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + 2 * n * (n - 1)


if __name__ == "__main__":
    test_cases = [((1,), 1), ((2,), 5)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().coloredCells(*args) == expected
