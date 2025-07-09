#
# @lc app=leetcode.cn id=75 lang=python3
# @lcpr version=30201
#
# [75] 颜色分类
#


# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 注意区间的开闭，初始化时区间内应该没有元素
        # 所以我们定义 [0，p0) 是元素 0 的区间，(p2, nums.length - 1] 是 2 的区间
        p0 = 0
        p2 = len(nums) - 1
        p = 0
        # 由于 p2 是开区间，所以 p <= p2
        while p <= p2:
            if nums[p] == 0:
                self.swap(nums, p0, p)
                p0 += 1
            elif nums[p] == 2:
                self.swap(nums, p2, p)
                p2 -= 1
            elif nums[p] == 1:
                p += 1

            # 因为小于 p0 都是 0，所以 p 不要小于 p0
            if p < p0:
                p = p0

    def swap(self, nums: List[int], i: int, j: int) -> None:
        nums[i], nums[j] = nums[j], nums[i]


# @lc code=end


#
# @lcpr case=start
# [2,0,2,1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [2,0,1]\n
# @lcpr case=end

#
