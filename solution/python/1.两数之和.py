#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return [i for i, num in enumerate(nums) if target - num in nums[i + 1 :]] + [i for i, num in enumerate(nums) if target - num in nums[:i]]


# @lc code=end
