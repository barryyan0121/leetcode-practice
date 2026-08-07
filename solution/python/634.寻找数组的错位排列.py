#
# @lc app=leetcode.cn id=634 lang=python3
#
# [634] 寻找数组的错位排列
#


# @lc code=start
class Solution:
    def findDerangement(self, n: int) -> int:
        mod = 10**9 + 7
        a, b = 1, 0
        for i in range(2, n + 1):
            a, b = b, (i - 1) * (a + b) % mod
        return b


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    assert solution.findDerangement(3) == 2
    assert solution.findDerangement(4) == 9
