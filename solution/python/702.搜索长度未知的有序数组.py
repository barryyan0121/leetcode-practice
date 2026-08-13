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

if __name__ == "__main__":
    class Reader:
        def __init__(self, values): self.values = values
        def get(self, index): return self.values[index] if index < len(self.values) else 2**31 - 1
    solver = Solution()
    assert solver.search(Reader([-1, 0, 3, 5, 9, 12]), 9) == 4
    assert solver.search(Reader([-1, 0, 3, 5, 9, 12]), 2) == -1


if __name__ == "__main__":
    class Reader:
        def __init__(self, nums):
            self.nums = nums

        def get(self, index):
            return self.nums[index] if index < len(self.nums) else 2147483647

    reader = Reader([-1, 0, 3, 5, 9, 12])
    assert Solution().search(reader, 9) == 4
    assert Solution().search(reader, 2) == -1
