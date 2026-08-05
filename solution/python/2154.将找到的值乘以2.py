"""2154. 将找到的值乘以 2"""


class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        values = set(nums)
        while original in values:
            original *= 2
        return original


if __name__ == "__main__":
    test_cases = [(([5, 3, 6, 1, 12], 3), 24)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().findFinalValue(*args) == expected
