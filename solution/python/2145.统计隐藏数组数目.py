"""2145. 统计隐藏数组数目"""


class Solution:
    def numberOfArrays(self, differences: list[int], lower: int, upper: int) -> int:
        current = minimum = maximum = 0
        for difference in differences:
            current += difference
            minimum = min(minimum, current)
            maximum = max(maximum, current)
        return max(0, (upper - lower) - (maximum - minimum) + 1)


if __name__ == "__main__":
    test_cases = [(([1, -3, 4], 1, 6), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().numberOfArrays(*args) == expected
