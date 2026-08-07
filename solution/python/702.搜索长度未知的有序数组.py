#
# @lc app=leetcode.cn id=702 lang=python3
#
# [702] 搜索长度未知的有序数组
#


# @lc code=start
class Solution:
    def search(self, reader, target: int) -> int:
        left, right = 0, 1
        while reader.get(right) < target:
            left, right = right, right * 2
        while left <= right:
            middle = (left + right) // 2
            value = reader.get(middle)
            if value == target:
                return middle
            if value < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1


# @lc code=end
