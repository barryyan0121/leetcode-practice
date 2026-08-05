"""2057. 最小下标"""


class Solution:
    def smallestEqual(self, nums: list[int]) -> int:
        return next((i for i, value in enumerate(nums) if i % 10 == value), -1)


if __name__ == "__main__":
    test_cases = [(([0, 1, 2],), 0), (([4, 3, 2, 1],), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().smallestEqual(*args) == expected
