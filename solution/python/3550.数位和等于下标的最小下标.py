"""3550. 数位和等于下标的最小下标"""


class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        for index, value in enumerate(nums):
            if sum(map(int, str(value))) == index:
                return index
        return -1


if __name__ == "__main__":
    test_cases = [
        (([1, 3, 2],), 2),
        (([1, 10, 11],), 1),
        (([1, 2, 3],), -1),
    ]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().smallestIndex(nums) == expected
