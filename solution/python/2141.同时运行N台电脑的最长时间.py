"""2141. 同时运行 N 台电脑的最长时间"""


class Solution:
    def maxRunTime(self, n: int, batteries: list[int]) -> int:
        low, high = 0, sum(batteries) // n
        while low < high:
            middle = (low + high + 1) // 2
            if sum(min(value, middle) for value in batteries) >= n * middle:
                low = middle
            else:
                high = middle - 1
        return low


if __name__ == "__main__":
    test_cases = [((2, [3, 3, 3]), 4)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maxRunTime(*args) == expected
