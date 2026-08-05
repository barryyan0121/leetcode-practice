"""2033. 获取单值网格的最小操作数"""


class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        values = [value for row in grid for value in row]
        if any((value - values[0]) % x for value in values):
            return -1
        values.sort()
        median = values[len(values) // 2]
        return sum(abs(value - median) // x for value in values)


if __name__ == "__main__":
    test_cases = [(([[2, 4], [6, 8]], 2), 4), (([[1, 2], [3, 4]], 2), -1)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minOperations(*args) == expected
