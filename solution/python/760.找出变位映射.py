#
# @lc app=leetcode.cn id=760 lang=python3
#
# [760] 找出变位映射
#


# @lc code=start
class Solution:
    def anagramMappings(self, nums1, nums2):
        positions = {}
        for index, value in enumerate(nums2):
            positions.setdefault(value, []).append(index)
        return [positions[value].pop() for value in nums1]


# @lc code=end


if __name__ == "__main__":
    assert sorted(
        Solution().anagramMappings([12, 28, 46, 32, 50], [50, 12, 32, 46, 28])
    ) == [0, 1, 2, 3, 4]
