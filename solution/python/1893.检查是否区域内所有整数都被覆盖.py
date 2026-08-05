"""1893. 检查是否区域内所有整数都被覆盖"""


class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        covered = [False] * (right - left + 1)
        for start, end in ranges:
            for value in range(max(start, left), min(end, right) + 1):
                covered[value - left] = True
        return all(covered)


if __name__ == "__main__":
    test_cases = [(([[1, 2], [3, 4], [5, 6]], 2, 5), True)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().isCovered(*args) == expected
