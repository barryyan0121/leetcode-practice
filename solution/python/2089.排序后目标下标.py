"""2089. 排序后目标下标"""

from bisect import bisect_left, bisect_right


class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        return list(range(bisect_left(nums, target), bisect_right(nums, target)))


if __name__ == "__main__":
    test_cases = [(([1, 2, 5, 2, 3], 2), [1, 2])]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().targetIndices(*args) == expected
