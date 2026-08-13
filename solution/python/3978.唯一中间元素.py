#
# @lc app=leetcode.cn id=3978 lang=python3
#
# [3978] 唯一中间元素
#


class Solution:
    # @lc code=start
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        middle = nums[len(nums) // 2]
        return nums.count(middle) == 1

    # @lc code=end


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3],), True),
        (([1, 2, 2],), False),
        (([7],), True),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().isMiddleElementUnique(*args) == expected
