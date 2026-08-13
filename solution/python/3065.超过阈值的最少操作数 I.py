"""3065. 超过阈值的最少操作数 I"""


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        return sum(value < k for value in nums)


if __name__ == "__main__":
    test_cases = [
        (([2, 11, 10, 1, 3], 10), 3),
        (([1, 1, 2, 4, 9], 1), 0),
        (([1, 1, 2, 4, 9], 9), 4),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minOperations(*args) == expected
