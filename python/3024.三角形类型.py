#
# @lc app=leetcode.cn id=3024 lang=python3
# @lcpr version=30201
#
# [3024] 三角形类型
#

# @lc code=start
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        elif nums[0] == nums[2]:
            return "equilateral"
        elif nums[0] == nums[1] or nums[1] == nums[2]:
            return "isosceles"
        else:
            return "scalene"

# @lc code=end



#
# @lcpr case=start
# [3,3,3]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,5]\n
# @lcpr case=end

#

