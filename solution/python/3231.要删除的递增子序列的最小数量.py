"""3231. 要删除的递增子序列的最小数量"""

from bisect import bisect_right


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        tails = []
        for number in nums:
            number = -number
            index = bisect_right(tails, number)
            if index == len(tails):
                tails.append(number)
            else:
                tails[index] = number
        return len(tails)


if __name__ == "__main__":
    test_cases = [
        ([5, 3, 1, 4, 2], 3),
        ([1, 2, 3, 4, 5], 1),
        ([5, 4, 3, 2, 1], 5),
    ]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().minOperations(nums) == expected
